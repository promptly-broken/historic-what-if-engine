from typing import List, Dict, Tuple, Optional, Any
import math
import sys
import os

# Ensure parent directory is in path to import scenario_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scenario_data import SCENARIOS

SPEAKER_NAMES = {
    "ides_of_march": "Julius Caesar",
    "trial_of_socrates": "Socrates",
    "fall_of_tenochtitlan": "Moctezuma II",
    "gunpowder_plot": "Guy Fawkes",
    "salem_witch_trials": "Judge Danforth",
    "romanovs": "Yakov Yurovsky",
    "operation_valkyrie": "General Fromm",
    "appomattox": "General Lee",
    "franz_ferdinand": "Franz Ferdinand",
    "cuban_missile_crisis": "President Kennedy"
}

SCENARIO_MILESTONES = {
    "ides_of_march": [
        {"key": "Paranoia", "min_val": 70, "event": "Caesar orders his lictors to secure the perimeter and watch Cassius closely."},
        {"key": "Trust", "max_val": 25, "event": "Caesar openly confronts his aides, questioning the Senate's true motives."},
        {"key": "Trust", "min_val": 80, "event": "Caesar boldly dismisses all augurs and warnings, declaring his fortune invincible."}
    ],
    "trial_of_socrates": [
        {"key": "Defiance", "min_val": 75, "event": "Socrates mocks the Athenian court, proclaiming he should be rewarded with free dining at the Prytaneum."},
        {"key": "Compliance", "min_val": 65, "event": "Socrates accepts that a modest fine might satisfy the laws of Athens."}
    ],
    "fall_of_tenochtitlan": [
        {"key": "Suspicion", "min_val": 70, "event": "Moctezuma secretly commands Cuitláhuac's Eagle and Jaguar warriors to prepare an ambush."},
        {"key": "Hospitality", "min_val": 75, "event": "Moctezuma bestows golden collars upon the Spanish captains, seeking divine favor."}
    ],
    "gunpowder_plot": [
        {"key": "Breaking", "min_val": 60, "event": "Guy Fawkes trembles under intense questioning and begins to drop hints of Catesby's safehouses."},
        {"key": "Defiance", "min_val": 80, "event": "Fawkes proudly cries that thirty-six barrels of powder would have blown Parliament back to the dark ages."}
    ],
    "salem_witch_trials": [
        {"key": "Doubt", "min_val": 65, "event": "Judge Danforth pauses the court, questioning whether spectral evidence can truly be admitted."},
        {"key": "Zeal", "min_val": 80, "event": "Danforth signs five new arrest warrants, warning that Lucifer has infected the entire congregation."}
    ],
    "romanovs": [
        {"key": "Greed", "min_val": 60, "event": "Yurovsky hesitates at the sound of White Army artillery, eyeing the Imperial jewels sewn in coats."},
        {"key": "Loyalty", "min_val": 80, "event": "Yurovsky reads the Soviet execution decree with absolute unblinking resolve."}
    ],
    "operation_valkyrie": [
        {"key": "Courage", "min_val": 65, "event": "General Fromm signs Operation Valkyrie mobilization orders to seize Berlin communications."},
        {"key": "Fear", "min_val": 75, "event": "Fromm locks himself in his office, dreading the news that Hitler may still be alive."}
    ],
    "appomattox": [
        {"key": "Desperation", "min_val": 65, "event": "Confederate officers propose scattering into the Blue Ridge Mountains for guerrilla resistance."},
        {"key": "Honor", "min_val": 75, "event": "General Lee resolves that nothing is left except to meet General Grant and accept honorable terms."}
    ],
    "franz_ferdinand": [
        {"key": "Panic", "min_val": 65, "event": "The Archduke orders the chauffeur to stop immediately and turn away from Appel Quay."},
        {"key": "Stubbornness", "min_val": 80, "event": "Franz Ferdinand angrily dismisses security concerns, insisting on visiting the hospital."}
    ],
    "cuban_missile_crisis": [
        {"key": "Hawkishness", "min_val": 70, "event": "DEFCON 2 is activated; Strategic Air Command prepares airstrikes on San Cristóbal."},
        {"key": "Diplomacy", "min_val": 70, "event": "President Kennedy dispatches Robert Kennedy to finalize the secret Turkish missile trade."}
    ]
}

DEFAULT_INITIAL_STATES = {
    "ides_of_march": {"Trust": 65, "Paranoia": 30},
    "trial_of_socrates": {"Compliance": 30, "Defiance": 70},
    "fall_of_tenochtitlan": {"Hospitality": 65, "Suspicion": 35},
    "gunpowder_plot": {"Defiance": 75, "Breaking": 20},
    "salem_witch_trials": {"Zeal": 75, "Doubt": 25},
    "romanovs": {"Loyalty": 75, "Greed": 20},
    "operation_valkyrie": {"Courage": 35, "Fear": 65},
    "appomattox": {"Honor": 75, "Desperation": 30},
    "franz_ferdinand": {"Stubbornness": 75, "Panic": 25},
    "cuban_missile_crisis": {"Diplomacy": 60, "Hawkishness": 35}
}

class GameStateManager:
    """
    Manages multi-scenario historical state, 3-Act dramatic narrative progression,
    dialogue history sliding window, dynamic prompt synthesis, and milestone events.
    """

    def __init__(self, scenario_name: str = "ides_of_march"):
        if scenario_name not in SCENARIOS:
            scenario_name = "ides_of_march"
            
        self.scenario_name = scenario_name
        self.scenario_config = SCENARIOS[scenario_name]
        self.speaker_name = self.scenario_config.get("speaker") or SPEAKER_NAMES.get(scenario_name, "Historical Figure")
        self.location = self.scenario_config.get("location", "Historic Location")
        self.date = self.scenario_config.get("date", "Historic Era")
        self.historical_context = self.scenario_config.get("historical_context", "")
        
        # State variables
        self.state: Dict[str, int] = DEFAULT_INITIAL_STATES.get(
            scenario_name,
            {k: 50 for k in self.scenario_config["state_keys"]}
        ).copy()
        
        # 3-Act Progression
        self.current_act = "act_1"
        self.unlocked_acts = ["act_1"]
        
        # Story so far timeline
        self.story_so_far: List[str] = list(self.scenario_config.get("hgtm_story", []))
        self.triggered_milestones: List[str] = []
        
        # Dialogue history
        self.dialogue_history: List[Dict[str, str]] = []
        self.max_dialogue_history = 6
        self.turn_count = 0

    def evaluate_act_progression(self) -> Optional[str]:
        """
        Evaluates dramatic progression across the 3 acts.
        Returns newly triggered act event description if an act threshold was just crossed.
        """
        progress = self.get_progress_percentage()
        acts_cfg = self.scenario_config.get("acts", {})
        
        new_act = self.current_act
        if (self.turn_count >= 4 or progress >= 70) and "act_3" in acts_cfg:
            new_act = "act_3"
        elif (self.turn_count >= 2 or progress >= 35) and "act_2" in acts_cfg:
            new_act = "act_2"
            
        if new_act != self.current_act and new_act not in self.unlocked_acts:
            self.current_act = new_act
            self.unlocked_acts.append(new_act)
            act_info = acts_cfg[new_act]
            event_text = f"TIMELINE ESCALATION — {act_info['name']}: {act_info['event']}"
            self.story_so_far.append(event_text)
            return event_text
            
        return None

    def update_state(self, deltas: Dict[str, int]) -> Tuple[Dict[str, int], Optional[str]]:
        """
        Applies state deltas, clamps values between 0 and 100, and checks
        if any milestone story events or Act escalations have been triggered.
        Returns: (actual_deltas_applied, newly_triggered_event_text)
        """
        applied_deltas = {}
        for key, delta in deltas.items():
            if key in self.state:
                old_val = self.state[key]
                new_val = max(0, min(100, old_val + delta))
                self.state[key] = new_val
                applied_deltas[key] = new_val - old_val

        # 1. Check for Act Escalations
        act_event = self.evaluate_act_progression()
        if act_event:
            return applied_deltas, act_event

        # 2. Check for State Threshold Milestones
        triggered_event = None
        milestones = SCENARIO_MILESTONES.get(self.scenario_name, [])
        for m in milestones:
            m_id = f"{m['key']}_{m.get('min_val', m.get('max_val'))}"
            if m_id in self.triggered_milestones:
                continue
                
            curr_val = self.state.get(m['key'], 50)
            if "min_val" in m and curr_val >= m["min_val"]:
                triggered_event = m["event"]
                self.triggered_milestones.append(m_id)
                self.story_so_far.append(triggered_event)
                break
            elif "max_val" in m and curr_val <= m["max_val"]:
                triggered_event = m["event"]
                self.triggered_milestones.append(m_id)
                self.story_so_far.append(triggered_event)
                break

        return applied_deltas, triggered_event

    def add_turn(self, player_text: str, npc_text: str):
        """Records a full conversational exchange."""
        self.dialogue_history.append({"speaker": "Player (Advisor)", "text": player_text})
        self.dialogue_history.append({"speaker": self.speaker_name, "text": npc_text})
        self.turn_count += 1
        
        # Maintain sliding window
        while len(self.dialogue_history) > self.max_dialogue_history:
            self.dialogue_history.pop(0)

    def select_active_persona(self) -> str:
        """
        Calculates the closest persona adapter based on Euclidean distance
        between current state variables and persona state range midpoints.
        """
        personas = self.scenario_config["personas"]
        best_persona = list(personas.keys())[0]
        min_distance = float("inf")

        for persona_name, persona_cfg in personas.items():
            dist_sq = 0.0
            ranges = persona_cfg.get("state_ranges", {})
            for key, val in self.state.items():
                if key in ranges:
                    lo, hi = ranges[key]
                    target_mid = (lo + hi) / 2.0
                    dist_sq += (val - target_mid) ** 2
                else:
                    dist_sq += (val - 50.0) ** 2
            
            if dist_sq < min_distance:
                min_distance = dist_sq
                best_persona = persona_name

        return best_persona

    def get_progress_percentage(self) -> int:
        """Calculates narrative progress towards timeline divergence (0-100%)."""
        base_progress = min(60, self.turn_count * 15)
        # Check polarization of state variables (distance from 50)
        polarization = sum(abs(v - 50) for v in self.state.values()) / (len(self.state) * 50)
        return min(100, int(base_progress + polarization * 40))

    def get_current_act_info(self) -> Dict[str, Any]:
        """Returns details of the currently active dramatic act."""
        acts = self.scenario_config.get("acts", {})
        if self.current_act in acts:
            return acts[self.current_act]
        return {
            "name": "Act I: The Flashpoint",
            "event": "The historical dilemma commences.",
            "dilemmas": []
        }

    def get_tactical_suggestions(self) -> List[Dict[str, str]]:
        """Returns 3 context-specific tactical dilemma chips for the current act."""
        act_info = self.get_current_act_info()
        dilemmas = act_info.get("dilemmas", [])
        if dilemmas:
            return dilemmas
        return [
            {"badge": "DELIBERATE", "label": "Weigh strategic alternatives", "prompt": "What are your orders in this hour?"},
            {"badge": "DE-ESCALATE", "label": "Counsel peaceful compromise", "prompt": "We must avoid bloodshed if possible."},
            {"badge": "CONFRONT", "label": "Demand immediate decisive action", "prompt": "We cannot afford hesitation; strike now!"}
        ]

    def format_prompt(self, persona_name: str, current_player_text: str) -> Tuple[str, str]:
        """
        Assembles system prompt and strictly structured user prompt block.
        CRUCIAL: Directly includes current_player_text in the dialogue so the NPC hears the player!
        """
        persona_cfg = self.scenario_config["personas"][persona_name]
        act_info = self.get_current_act_info()
        
        # Enhanced System Instructions
        system_prompt = (
            f"{persona_cfg['system']}\n"
            f"HISTORICAL GROUNDING: {self.historical_context}\n"
            f"CURRENT DRAMATIC STAGE: {act_info['name']} — {act_info['event']}\n"
            f"BANNED CONCEPTS: {self.scenario_config.get('banned', '')}\n"
            "MANDATORY INSTRUCTIONS:\n"
            f"1. CONVERSATIONAL AUDIENCE: You are {self.speaker_name}. You are speaking directly to the Player (your trusted counselor or cabinet advisor seated with you in {self.location}). Address the Player directly (e.g., debate their counsel, weigh their proposed risks, or deliver your executive orders to them). Third parties mentioned (e.g. foreign ministers, opposing rulers, distant generals) are NOT in the room—do not address them as if they are present.\n"
            "2. ANTI-PARROTING MANDATE: NEVER repeat, echo, or parrot the Player's opening words, sentences, or phrasing. Do not begin your response by reciting what the Player just advised. Jump immediately into your own independent tactical analysis, objections, strategic doubts, or decisive decree.\n"
            "3. Ground your speech in historical reality, citing real names, places, weapons, and beliefs.\n"
            "4. Let your tone reflect your internal psychological state (fear, arrogance, suspicion, honor).\n"
            "5. Never repeat canned formulas or clichés. Speak with living historical conviction.\n"
            "6. Deliver a complete response within 2-3 focused paragraphs. Always conclude with complete sentences."
        )

        state_str = "\n".join([f"- {k}: {v}/100" for k, v in self.state.items()])
        story_str = "\n".join([f"- {event}" for event in self.story_so_far[-5:]])

        dialogue_str = ""
        for turn in self.dialogue_history[-4:]:
            dialogue_str += f"{turn['speaker']}: {turn['text']}\n\n"
        
        # Include current player turn explicitly!
        dialogue_str += f"Player (Advisor): {current_player_text}\n"

        prompt_block = f"""[WORLD & PSYCHOLOGICAL STATE]
{state_str}

[CURRENT ESCALATION: {act_info['name']}]
{act_info['event']}

[STORY SO FAR]
{story_str}

[RECENT DIALOGUE]
{dialogue_str}
[YOUR TASK]
Respond in-character as {self.speaker_name} directly to your advisor (the Player).
Address their strategic counsel with your own distinct perspective, doubts, or orders.
CRITICAL: Under no circumstances should you repeat or echo their opening words or phrasing."""

        return system_prompt, prompt_block

    def get_summary_dict(self) -> Dict[str, Any]:
        """Returns the full serializable state dictionary."""
        active_persona = self.select_active_persona()
        act_info = self.get_current_act_info()
        return {
            "scenario_id": self.scenario_name,
            "speaker": self.speaker_name,
            "location": self.location,
            "date": self.date,
            "state": self.state,
            "current_act": self.current_act,
            "act_name": act_info["name"],
            "act_event": act_info["event"],
            "active_persona": active_persona,
            "story_so_far": self.story_so_far,
            "progress": self.get_progress_percentage(),
            "turn_count": self.turn_count,
            "suggestions": self.get_tactical_suggestions(),
            "dialogue_history": self.dialogue_history
        }
