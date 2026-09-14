from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import os
import sys

# Ensure dynamic_npc_engine directory is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Only enable offline mode if the model is already downloaded locally to avoid network hangs;
# fresh users will automatically download it on first launch.
hf_cache = os.path.expanduser("~/.cache/huggingface/hub/models--mlx-community--Qwen2.5-7B-Instruct-4bit")
if os.path.exists(hf_cache):
    os.environ["HF_HUB_OFFLINE"] = "1"

from scenario_data import SCENARIOS
from api.game_state import GameStateManager, SPEAKER_NAMES
from api.evaluator import StateEvaluator

app = FastAPI(title="Historic What-If Dynamic Narrative Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model state
MODEL_ID = "mlx-community/Qwen2.5-7B-Instruct-4bit"
model = None
tokenizer = None
current_loaded_adapter = None
USE_OVERFITTED_LORA = os.environ.get("USE_LORA", "false").lower() == "true"

# Active game sessions: scenario_id -> GameStateManager
active_sessions: Dict[str, GameStateManager] = {}
current_scenario_id = "ides_of_march"

OPENING_LINES = {
    "ides_of_march": "The Senate must be convinced. The future of Rome is within our grasp. What whisperings have reached your ears today?",
    "trial_of_socrates": "The citizens of Athens have gathered to judge my life. Tell me, friend, do you believe virtue can be taught, or is it innate to the soul?",
    "fall_of_tenochtitlan": "The bearded strangers from across the eastern sea march with our ancient Tlaxcalan foes. Are they gods or mortal conquerors?",
    "gunpowder_plot": "Who lurks in the dark of this undercroft? Speak! The fuse is dry, and thirty-six barrels await the flame.",
    "salem_witch_trials": "The court of Oyer and Terminer is now seated. Speak with the fear of God before you, for the devil has laid siege to Massachusetts.",
    "romanovs": "The Ural Soviet decree is written. The White Army's guns rumble outside Yekaterinburg, and time runs thin in the Ipatiev cellar.",
    "operation_valkyrie": "The Wolf's Lair telegram cables have been severed! Stauffenberg claims Hitler is dead, yet the Propaganda Ministry claims otherwise. What do we do?",
    "appomattox": "The lines are broken, and the Army of Northern Virginia is surrounded and starving. What terms can we salvage from General Grant?",
    "franz_ferdinand": "A morning grenade will not keep me from my duty to the wounded officers. Chauffeur, guide us along the quay!",
    "cuban_missile_crisis": "The U-2 reconnaissance photos leave no doubt—nuclear launch sites in San Cristóbal. The Joint Chiefs urge an immediate air strike."
}

def get_or_create_session(scenario_id: str) -> GameStateManager:
    global current_scenario_id
    if scenario_id not in SCENARIOS:
        scenario_id = "ides_of_march"
    current_scenario_id = scenario_id
    if scenario_id not in active_sessions:
        active_sessions[scenario_id] = GameStateManager(scenario_id)
    return active_sessions[scenario_id]

@app.on_event("startup")
async def startup_event():
    global model, tokenizer
    print(f"Loading base model {MODEL_ID} into unified memory...")
    try:
        from mlx_lm import load
        model, tokenizer = load(MODEL_ID)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Warning: MLX model load encountered an issue: {e}. Running in simulation/fallback mode.")

class ScenarioStartRequest(BaseModel):
    scenario_id: str

class ChatRequest(BaseModel):
    prompt: str
    scenario_id: Optional[str] = None
    state: Optional[str] = None  # Backward compatibility for direct adapter override

@app.get("/")
def root():
    return {
        "status": "online",
        "game": "Historic What-If: Dynamic Narrative Engine",
        "current_scenario": current_scenario_id,
        "scenarios_available": list(SCENARIOS.keys())
    }

@app.get("/scenarios")
def list_scenarios():
    catalog = []
    for s_id, s_cfg in SCENARIOS.items():
        acts = s_cfg.get("acts", {})
        act1_info = acts.get("act_1", {})
        catalog.append({
            "id": s_id,
            "title": s_cfg.get("title", s_id.replace("_", " ").title()),
            "speaker": s_cfg.get("speaker") or SPEAKER_NAMES.get(s_id, "Historical Figure"),
            "location": s_cfg.get("location", ""),
            "date": s_cfg.get("date", ""),
            "state_keys": s_cfg.get("state_keys", []),
            "opening_line": OPENING_LINES.get(s_id, "Greetings."),
            "hgtm_story": s_cfg.get("hgtm_story", []),
            "historical_context": s_cfg.get("historical_context", ""),
            "acts_count": len(acts),
            "act_1_name": act1_info.get("name", "Act I")
        })
    return {"scenarios": catalog}

@app.post("/scenario/start")
def start_scenario(request: ScenarioStartRequest):
    s_id = request.scenario_id
    if s_id not in SCENARIOS:
        raise HTTPException(status_code=404, detail=f"Scenario '{s_id}' not found.")
    
    # Reset session for fresh start
    active_sessions[s_id] = GameStateManager(s_id)
    gsm = active_sessions[s_id]
    
    opening = OPENING_LINES.get(s_id, "Greetings.")
    act_info = gsm.get_current_act_info()
    suggestions = gsm.get_tactical_suggestions()
    
    return {
        "scenario_id": s_id,
        "speaker": gsm.speaker_name,
        "location": gsm.location,
        "date": gsm.date,
        "state": gsm.state,
        "current_act": gsm.current_act,
        "act_name": act_info["name"],
        "act_event": act_info["event"],
        "active_persona": gsm.select_active_persona(),
        "story_so_far": gsm.story_so_far,
        "opening_line": opening,
        "progress": gsm.get_progress_percentage(),
        "suggestions": suggestions
    }

@app.get("/state")
def get_current_state(scenario_id: Optional[str] = None):
    s_id = scenario_id or current_scenario_id
    gsm = get_or_create_session(s_id)
    return gsm.get_summary_dict()

@app.post("/chat")
def chat(request: ChatRequest):
    global model, tokenizer, current_loaded_adapter
    
    # Check if this is legacy merchant/guard call
    if request.state and not request.scenario_id:
        return handle_legacy_chat(request)
        
    s_id = request.scenario_id or current_scenario_id
    gsm = get_or_create_session(s_id)
    player_text = request.prompt.strip()
    
    if not player_text:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    # 1. State Evaluation (The Invisible Evaluator)
    deltas, rationale = StateEvaluator.evaluate(player_text, s_id, gsm.state)
    applied_deltas, milestone_event = gsm.update_state(deltas)
    
    # 2. Select Dynamic Persona
    active_persona = gsm.select_active_persona()
    
    # 3. Optional LoRA Adapter Management
    if model and USE_OVERFITTED_LORA:
        adapter_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "adapters", active_persona))
        try:
            from mlx_lm.tuner.utils import remove_lora_layers, load_adapters
            if current_loaded_adapter != active_persona:
                model = remove_lora_layers(model)
                if os.path.exists(adapter_path):
                    model = load_adapters(model, adapter_path)
                    current_loaded_adapter = active_persona
                    print(f"Hot-swapped to LoRA adapter: {active_persona}")
                else:
                    current_loaded_adapter = None
        except Exception as e:
            print(f"LoRA swap warning: {e}")
    elif model and current_loaded_adapter is not None:
        try:
            from mlx_lm.tuner.utils import remove_lora_layers
            model = remove_lora_layers(model)
            current_loaded_adapter = None
        except Exception as e:
            print(f"Adapter removal warning: {e}")

    # 4. Assemble Grounded Prompt with Player's Exact Input!
    system_prompt, user_prompt = gsm.format_prompt(active_persona, player_text)
    
    # 5. Generate Dynamic In-Character Response
    npc_response = "..."
    if model and tokenizer:
        from mlx_lm import generate
        from mlx_lm.sample_utils import make_sampler
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        formatted_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        raw_response = generate(
            model,
            tokenizer,
            prompt=formatted_prompt,
            max_tokens=220,
            sampler=make_sampler(temp=0.7),
            verbose=False
        )
        
        # Clean response tags
        npc_response = raw_response.strip()
        if "<|im_start|>assistant" in npc_response:
            npc_response = npc_response.split("<|im_start|>assistant")[-1]
        npc_response = npc_response.replace("<|im_end|>", "").strip()
        
        # Remove any lingering "NPC:" prefix
        if npc_response.startswith("NPC:"):
            npc_response = npc_response[4:].strip()
    else:
        # Simulation fallback
        npc_response = f"[{gsm.speaker_name} considers your words deeply]: {rationale} We shall deliberate further on this course."

    # 6. Record Dialogue Turn
    gsm.add_turn(player_text, npc_response)
    
    # 7. Retrieve Context-Specific Tactical Suggestions for the Current Act
    act_info = gsm.get_current_act_info()
    suggestions = gsm.get_tactical_suggestions()
    
    return {
        "response": npc_response,
        "speaker": gsm.speaker_name,
        "active_persona": active_persona,
        "current_act": gsm.current_act,
        "act_name": act_info["name"],
        "act_event": act_info["event"],
        "state": gsm.state,
        "deltas": applied_deltas,
        "rationale": rationale,
        "milestone": milestone_event,
        "story_so_far": gsm.story_so_far,
        "progress": gsm.get_progress_percentage(),
        "suggestions": suggestions
    }

def handle_legacy_chat(request: ChatRequest):
    global model, tokenizer, current_loaded_adapter
    adapter_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "adapters", request.state))
    if model:
        from mlx_lm.tuner.utils import remove_lora_layers, load_adapters
        from mlx_lm import generate
        from mlx_lm.sample_utils import make_sampler
        if current_loaded_adapter != request.state:
            model = remove_lora_layers(model)
            if os.path.exists(adapter_path):
                model = load_adapters(model, adapter_path)
                current_loaded_adapter = request.state
        
        messages = [
            {"role": "system", "content": f"You are a character in state {request.state}."},
            {"role": "user", "content": request.prompt}
        ]
        formatted_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        raw = generate(model, tokenizer, prompt=formatted_prompt, max_tokens=150, sampler=make_sampler(temp=0.7))
        resp = raw.split("<|im_start|>assistant")[-1].replace("<|im_end|>", "").strip()
        return {"response": resp, "state": request.state}
    return {"response": "Mock reply", "state": request.state}
