import re
from typing import Dict, List, Tuple, Any, Optional
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scenario_data import SCENARIOS

class StateEvaluator:
    """
    The Invisible Evaluator:
    Analyzes semantic meaning, historical rhetoric, and player intent in real time.
    Calculates nuanced numerical state deltas (-25 to +25) for scenario variables,
    generates psychologically grounded rationales, and provides Act-aware tactical dilemma chips.
    """

    # Expanded intent patterns capturing historical vocabulary, military orders, and philosophical arguments
    INTENT_PATTERNS = {
        "military_strike": [
            r"\b(cavalry|causeway|causeways|cut down|seal|ambush|attack|strike|charge|slaughter|bayonet|bayonets|flank|breakout|assault|bomb|missile|missiles|war|kill|destroy|invade|mobilize|army|weapons|swords|spears|macuahuitl|panzer|panzers|force|fire)\b",
            r"\b(take up arms|wipe them out|fight to the last|destroy them|strike now|no white flags)\b"
        ],
        "sacred_omen_augury": [
            r"\b(smoking mirror|calendar|omen|omens|augur|haruspex|foretell|prophecy|priest|priests|gods|deity|huitzilopochtli|quetzalcoatl|tezcatlipoca|spurinna|daemon|teocalli|templo|sacrifice|divine|providence|heavens|blessing)\b",
            r"\b(will of the gods|fifth sun|holy church|god will judge|calpurnia's dream)\b"
        ],
        "espionage_conspiracy": [
            r"\b(spy|spies|traitor|traitors|secret|secrets|conspiracy|conspirators|plot|plotting|dagger|daggers|steel|toga|cassius|brutus|catesby|treason|infiltrate|undercover|malice|treachery|hidden|whisper|assassin|assassins)\b",
            r"\b(watch your back|do not trust|trap|ambush ahead|someone will kill you)\b"
        ],
        "diplomatic_parley": [
            r"\b(treaty|peace|gift|gifts|tribute|parley|parole|surrender|terms|compromise|negotiate|backchannel|trade|mercy|pact|quarantine|neutral|ceasefire|pardon|spare|save face|de-escalate|withdraw)\b",
            r"\b(spare their lives|avoid bloodshed|talk to them|let them go|peaceful solution)\b"
        ],
        "bribery_wealth": [
            r"\b(bribe|gold|diamonds|jewels|treasure|riches|fortune|wealth|money|silver|corset|corsets|payment|safe passage)\b",
            r"\b(buy your way|keep the gold|offer them riches)\b"
        ],
        "philosophical_inquiry": [
            r"\b(virtue|wisdom|truth|examine|logic|corrupt|youth|meletus|elenchus|unexamined|hemlock|law|laws|justice|proof|evidence|reason|soul|covenant|spectral|infallible|moral)\b",
            r"\b(what is virtue|why do you question|is it right|examine yourself)\b"
        ],
        "warning_danger": [
            r"\b(danger|flee|escape|turn back|cancel|do not go|stay home|hide|beware|threat|death trap|run|hurry|reverse)\b",
            r"\b(your life is in danger|they are coming for you|leave now|save yourself)\b"
        ],
        "flattery_arrogance": [
            r"\b(invincible|conqueror|greatness|destiny|beloved|divine favor|unconquerable|glory|monarch|majesty|emperor|caesar)\b",
            r"\b(you cannot be defeated|you are the master|they tremble before you)\b"
        ]
    }

    # Scenario-specific delta weighting and dynamic reaction rationales
    SCENARIO_RULES = {
        "ides_of_march": {
            "primary": ("Trust", "Paranoia"),
            "speaker": "Caesar",
            "reactions": {
                "espionage_conspiracy": ({"Trust": -20, "Paranoia": +25}, "Caesar's gaze narrows, his thoughts racing to the hidden daggers of the Senate."),
                "warning_danger": ({"Trust": -15, "Paranoia": +20}, "Caesar feels a chill of mortal vulnerability at the dark portents."),
                "flattery_arrogance": ({"Trust": +20, "Paranoia": -20}, "Caesar's chin rises with imperial pride, dismissing mortal fears as unworthy of his fortune."),
                "diplomatic_parley": ({"Trust": +10, "Paranoia": -10}, "Caesar considers the value of clemency, recalling his forgiveness of past enemies."),
                "military_strike": ({"Trust": -10, "Paranoia": +15}, "Caesar calculates the deployment of his veteran legions across the Tiber."),
                "philosophical_inquiry": ({"Trust": +5, "Paranoia": +5}, "Caesar weighs your counsel with the strategic intellect of the Commentaries.")
            }
        },
        "trial_of_socrates": {
            "primary": ("Compliance", "Defiance"),
            "speaker": "Socrates",
            "reactions": {
                "philosophical_inquiry": ({"Compliance": +10, "Defiance": +15}, "Socrates smiles with genuine delight, eager to cross-examine this philosophical claim."),
                "diplomatic_parley": ({"Compliance": +20, "Defiance": -15}, "Socrates considers your plea for moderation, weighing the peace of Athens against truth."),
                "warning_danger": ({"Compliance": -5, "Defiance": +15}, "Socrates shrugs off the fear of death, declaring that to fear death is false wisdom."),
                "military_strike": ({"Compliance": -20, "Defiance": +20}, "Socrates rebukes the notion of violence, upholding the examined life over force."),
                "espionage_conspiracy": ({"Compliance": -10, "Defiance": +15}, "Socrates scorns the political machinations of Meletus and Anytus.")
            }
        },
        "fall_of_tenochtitlan": {
            "primary": ("Hospitality", "Suspicion"),
            "speaker": "Moctezuma II",
            "reactions": {
                "military_strike": ({"Hospitality": -25, "Suspicion": +25}, "Moctezuma's pulse quickens as Cuitláhuac's war drums echo across Lake Texcoco."),
                "espionage_conspiracy": ({"Hospitality": -20, "Suspicion": +25}, "Moctezuma's brow furrows in dread as the deceit of the bearded strangers is laid bare."),
                "sacred_omen_augury": ({"Hospitality": +10, "Suspicion": +15}, "Moctezuma gazes toward the Templo Mayor, searching the heavens for the will of the Fifth Sun."),
                "diplomatic_parley": ({"Hospitality": +20, "Suspicion": -15}, "Moctezuma breathes a breath of relief, hoping golden gifts may yet avert ruin on the lake."),
                "bribery_wealth": ({"Hospitality": +15, "Suspicion": -10}, "Moctezuma orders chests of quetzal plumes and golden disks prepared for the strangers."),
                "warning_danger": ({"Hospitality": -15, "Suspicion": +20}, "Moctezuma remembers the weeping woman of the night omen, foretelling the fall of Tenochtitlan.")
            }
        },
        "gunpowder_plot": {
            "primary": ("Defiance", "Breaking"),
            "speaker": "Guy Fawkes",
            "reactions": {
                "military_strike": ({"Defiance": +25, "Breaking": -15}, "Fawkes sneers in defiance, boasting that 36 barrels would have leveled the heretic realm."),
                "warning_danger": ({"Defiance": -10, "Breaking": +20}, "Fawkes winces, the cold dread of the Tower rack tightening in his chest."),
                "diplomatic_parley": ({"Defiance": -15, "Breaking": +20}, "Fawkes hesitates, weighing King James's promises against his solemn Catholic oath."),
                "espionage_conspiracy": ({"Defiance": +15, "Breaking": +10}, "Fawkes grits his teeth, determined to shield Robert Catesby's identity to the death.")
            }
        },
        "salem_witch_trials": {
            "primary": ("Zeal", "Doubt"),
            "speaker": "Judge Danforth",
            "reactions": {
                "philosophical_inquiry": ({"Zeal": -20, "Doubt": +25}, "Danforth frowns deeply, shaken by the logical inconsistencies of spectral evidence."),
                "espionage_conspiracy": ({"Zeal": +20, "Doubt": -10}, "Danforth bangs his gavel, declaring that Satan's plot against Massachusetts will be crushed."),
                "diplomatic_parley": ({"Zeal": -15, "Doubt": +20}, "Danforth pauses as the petitions of honest Christian neighbors are read aloud."),
                "warning_danger": ({"Zeal": +15, "Doubt": -5}, "Danforth fears that showing weakness will invite the prince of darkness to conquer Salem.")
            }
        },
        "romanovs": {
            "primary": ("Loyalty", "Greed"),
            "speaker": "Yurovsky",
            "reactions": {
                "bribery_wealth": ({"Loyalty": -20, "Greed": +25}, "Yurovsky's eyes flicker to the glittering corsets of the grand duchesses with sharp calculation."),
                "diplomatic_parley": ({"Loyalty": -15, "Greed": +15}, "Yurovsky glances at his watch, measuring the distance to Moscow against the Czech Legion guns."),
                "military_strike": ({"Loyalty": +25, "Greed": -15}, "Yurovsky checks the chamber of his Nagant revolver with revolutionary finality."),
                "warning_danger": ({"Loyalty": +15, "Greed": +10}, "Yurovsky stiffens at the thought of a White Army counter-revolutionary rescue.")
            }
        },
        "operation_valkyrie": {
            "primary": ("Courage", "Fear"),
            "speaker": "General Fromm",
            "reactions": {
                "military_strike": ({"Courage": +25, "Fear": -15}, "Fromm hears the thunder of Reserve Army tanks securing the Berlin government quarter."),
                "warning_danger": ({"Courage": -20, "Fear": +25}, "Fromm breaks into a cold sweat, terrified that Hitler has survived the bomb at Rastenburg."),
                "espionage_conspiracy": ({"Courage": -15, "Fear": +20}, "Fromm trembles at the thought of Himmler's Gestapo discovering his silent complicity."),
                "diplomatic_parley": ({"Courage": +15, "Fear": -10}, "Fromm calculates the terms an anti-Nazi German government might negotiate with the Western Allies.")
            }
        },
        "appomattox": {
            "primary": ("Honor", "Desperation"),
            "speaker": "General Lee",
            "reactions": {
                "diplomatic_parley": ({"Honor": +25, "Desperation": -20}, "Lee nods with quiet sorrow, resolved to spare his starving boys any further pointless slaughter."),
                "military_strike": ({"Honor": -15, "Desperation": +25}, "Lee's hand grips the hilt of his sword as his younger officers urge one final suicidal charge."),
                "warning_danger": ({"Honor": +10, "Desperation": +15}, "Lee feels the encirclement of Sheridan's cavalry and Ord's infantry like a tightening vise.")
            }
        },
        "franz_ferdinand": {
            "primary": ("Stubbornness", "Panic"),
            "speaker": "Franz Ferdinand",
            "reactions": {
                "warning_danger": ({"Stubbornness": -20, "Panic": +25}, "The Archduke pales, suddenly realizing the motorcade has been steered into an assassin's trap."),
                "military_strike": ({"Stubbornness": +25, "Panic": -10}, "Franz Ferdinand demands Governor Potiorek clear the quay with drawn imperial bayonets."),
                "flattery_arrogance": ({"Stubbornness": +20, "Panic": -15}, "The Archduke scoffs at fear, boasting that the house of Habsburg does not bow to Serbian malcontents.")
            }
        },
        "cuban_missile_crisis": {
            "primary": ("Diplomacy", "Hawkishness"),
            "speaker": "President Kennedy",
            "reactions": {
                "diplomatic_parley": ({"Diplomacy": +25, "Hawkishness": -20}, "JFK leans back in his leather chair, focusing on the secret Turkish missile trade with Dobrynin."),
                "military_strike": ({"Diplomacy": -25, "Hawkishness": +25}, "Kennedy's jaw sets firmly as the Joint Chiefs urge an immediate 500-sortie air strike."),
                "warning_danger": ({"Diplomacy": +15, "Hawkishness": +10}, "Kennedy calculates the 100-million casualty projections of a thermonuclear exchange.")
            }
        }
    }

    @classmethod
    def evaluate(cls, player_input: str, scenario_id: str, current_state: Dict[str, int]) -> Tuple[Dict[str, int], str]:
        """
        Analyzes the player's text, matches historical and psychological intents,
        applies proportional state deltas, and produces an authentic character rationale.
        """
        lower_input = player_input.lower().strip()
        matched_intents = []

        # Check matched intent patterns
        for intent_name, patterns in cls.INTENT_PATTERNS.items():
            for pat in patterns:
                if re.search(pat, lower_input, re.IGNORECASE):
                    matched_intents.append(intent_name)
                    break

        scenario_info = cls.SCENARIO_RULES.get(scenario_id, cls.SCENARIO_RULES["ides_of_march"])
        primary_keys = scenario_info["primary"]
        reactions = scenario_info["reactions"]
        speaker = scenario_info.get("speaker", "The leader")
        
        accumulated_deltas: Dict[str, int] = {k: 0 for k in primary_keys}
        rationale_list: List[str] = []

        for intent_name in matched_intents:
            if intent_name in reactions:
                deltas, rationale = reactions[intent_name]
                for k, v in deltas.items():
                    if k in accumulated_deltas:
                        accumulated_deltas[k] += v
                rationale_list.append(rationale)

        # Fallback if no specific historical keywords matched: contextual tone inference
        if not matched_intents:
            if "?" in lower_input:
                accumulated_deltas[primary_keys[0]] = accumulated_deltas.get(primary_keys[0], 0) + 5
                accumulated_deltas[primary_keys[1]] = accumulated_deltas.get(primary_keys[1], 0) - 5
                rationale_list.append(f"{speaker} listens intently to your probing inquiry.")
            elif "!" in lower_input:
                accumulated_deltas[primary_keys[1]] = accumulated_deltas.get(primary_keys[1], 0) + 10
                accumulated_deltas[primary_keys[0]] = accumulated_deltas.get(primary_keys[0], 0) - 5
                rationale_list.append(f"{speaker} stiffens under the urgent pressure of your command.")
            else:
                accumulated_deltas[primary_keys[0]] = accumulated_deltas.get(primary_keys[0], 0) + 5
                rationale_list.append(f"{speaker} turns your counsel over in quiet contemplation.")

        # Clamp individual deltas to [-25, 25]
        clamped_deltas = {
            k: max(-25, min(25, v)) for k, v in accumulated_deltas.items()
        }

        final_rationale = rationale_list[0] if rationale_list else f"{speaker} weighs the gravity of your words."
        return clamped_deltas, final_rationale

    @classmethod
    def get_contextual_suggestions(cls, scenario_id: str, state: Dict[str, int], current_act: str = "act_1") -> List[Dict[str, str]]:
        """
        Returns 3 context-specific tactical dilemma chips tailored to the scenario and current act.
        """
        scenario = SCENARIOS.get(scenario_id, {})
        acts = scenario.get("acts", {})
        if current_act in acts and "dilemmas" in acts[current_act]:
            return acts[current_act]["dilemmas"]
        elif "act_1" in acts and "dilemmas" in acts["act_1"]:
            return acts["act_1"]["dilemmas"]
            
        return [
            {"badge": "DELIBERATE", "label": "Weigh strategic alternatives", "prompt": "What are your orders in this hour?"},
            {"badge": "DE-ESCALATE", "label": "Counsel peaceful compromise", "prompt": "We must avoid bloodshed if possible."},
            {"badge": "CONFRONT", "label": "Demand immediate decisive action", "prompt": "We cannot afford hesitation; strike now!"}
        ]
