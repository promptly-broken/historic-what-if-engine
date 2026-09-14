import sys
import os

# Add dynamic_npc_engine directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from api.server import app
from api.evaluator import StateEvaluator
from api.game_state import GameStateManager
from scenario_data import SCENARIOS

client = TestClient(app)

def test_evaluator_intents():
    # Warning & Conspiracy -> Paranoia increase, Trust decrease
    deltas, rationale = StateEvaluator.evaluate(
        "Caesar, beware! A deadly conspiracy has taken root among the senators.",
        "ides_of_march",
        {"Trust": 50, "Paranoia": 30}
    )
    assert deltas["Paranoia"] > 0, "Paranoia should increase on warning"
    assert deltas["Trust"] < 0, "Trust should decrease on warning"
    assert "daggers" in rationale.lower() or "senate" in rationale.lower() or "warning" in rationale.lower()

    # Reassurance & Divine Glory -> Trust increase, Paranoia decrease
    deltas_reassure, _ = StateEvaluator.evaluate(
        "Fear not, Gaius. Rome loves you, and your friends stand by your honor. You are unconquerable.",
        "ides_of_march",
        {"Trust": 50, "Paranoia": 30}
    )
    assert deltas_reassure["Trust"] > 0
    assert deltas_reassure["Paranoia"] < 0

def test_game_state_transitions():
    gsm = GameStateManager("ides_of_march")
    assert gsm.select_active_persona() == "caesar_arrogant"
    assert gsm.current_act == "act_1"
    assert len(gsm.get_tactical_suggestions()) == 3
    
    # Apply severe paranoia delta
    applied, milestone = gsm.update_state({"Trust": -40, "Paranoia": +55})
    assert gsm.state["Paranoia"] >= 70
    assert gsm.select_active_persona() == "caesar_paranoid"
    assert milestone is not None, "Milestone event or escalation should have triggered"

def test_api_scenarios_catalog():
    res = client.get("/scenarios")
    assert res.status_code == 200
    data = res.json()
    assert "scenarios" in data
    assert len(data["scenarios"]) == 10
    
    scenario_ids = [s["id"] for s in data["scenarios"]]
    assert "ides_of_march" in scenario_ids
    assert "trial_of_socrates" in scenario_ids
    assert "cuban_missile_crisis" in scenario_ids

def test_api_scenario_start():
    res = client.post("/scenario/start", json={"scenario_id": "trial_of_socrates"})
    assert res.status_code == 200
    data = res.json()
    assert data["scenario_id"] == "trial_of_socrates"
    assert data["speaker"] == "Socrates"
    assert "Compliance" in data["state"]
    assert "Defiance" in data["state"]
    assert len(data["suggestions"]) == 3
    assert len(data["story_so_far"]) > 0

def test_api_chat_flow():
    # Start Caesar scenario
    client.post("/scenario/start", json={"scenario_id": "ides_of_march"})
    
    # Send a warning message
    res = client.post("/chat", json={
        "scenario_id": "ides_of_march",
        "prompt": "Caesar, you must stay away from the Theatre of Pompey. Cassius carries a hidden dagger!"
    })
    assert res.status_code == 200
    data = res.json()
    assert "response" in data
    assert data["speaker"] == "Julius Caesar"
    assert "deltas" in data
    assert data["deltas"]["Paranoia"] > 0
    assert len(data["suggestions"]) == 3
    assert data["progress"] > 0

if __name__ == "__main__":
    print("Running verification suite...")
    test_evaluator_intents()
    print("✓ StateEvaluator intent tests passed!")
    test_game_state_transitions()
    print("✓ GameStateManager transition & milestone tests passed!")
    test_api_scenarios_catalog()
    print("✓ GET /scenarios catalog tests passed (10 scenarios)!")
    test_api_scenario_start()
    print("✓ POST /scenario/start endpoint tests passed!")
    test_api_chat_flow()
    print("✓ POST /chat full game loop tests passed!")
    print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")
