"""
Historic What-If: Dynamic Narrative Engine
Ground Truth Historical Matrix (HGTM) & Scenario Specifications
"""

SCENARIOS = {
    "ides_of_march": {
        "title": "The Ides of March",
        "speaker": "Julius Caesar",
        "location": "Rome, Theatre of Pompey",
        "date": "March 15, 44 BC",
        "historical_context": (
            "Julius Caesar has been named Dictator Perpetuo of the Roman Republic. A faction of approximately "
            "sixty senators led by Marcus Junius Brutus and Gaius Cassius Longinus believe Caesar seeks to crown "
            "himself King (Rex), destroying the 450-year-old Republic. Caesar has dismissed his Spanish bodyguard. "
            "The Senate meets today at the Curia of Pompey because the Senate House (Curia Hostilia) is being rebuilt."
        ),
        "hgtm_story": [
            "Caesar recently declared Dictator Perpetuo of Rome.",
            "Spurinna the haruspex warned Caesar to 'Beware the Ides of March'.",
            "Calpurnia woke weeping from a nightmare of Caesar's statue spouting blood."
        ],
        "banned": "Guns, modern democracy, English idioms, cellphones, feudalism, medieval castles.",
        "state_keys": ["Trust", "Paranoia"],
        "acts": {
            "act_1": {
                "name": "Act I: Omens & The Senate Summons",
                "event": "Caesar prepares his litter at the Domus Publica. Spurinna's warning hangs over Rome.",
                "dilemmas": [
                    {
                        "badge": "HEED CALPURNIA",
                        "label": "Urge him to stay home for Calpurnia's tears",
                        "prompt": "Caesar, heed Calpurnia's tears. Postpone the Senate and send Mark Antony to dismiss the senators today."
                    },
                    {
                        "badge": "EXPOSE CASSIUS",
                        "label": "Warn of Cassius and the secret dagger faction",
                        "prompt": "Gaius, Cassius gathers bitter senators in Pompey's portico! They conceal blades beneath their togas!"
                    },
                    {
                        "badge": "DIVINE DESTINY",
                        "label": "Flatter his martial glory and invincible fortune",
                        "prompt": "You are Caesar, conqueror of Gaul and victor of Pharsalus! The Senate grovels before your divine fortune."
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Steps of the Curia",
                "event": "Caesar arrives outside Pompey's Theatre. Trebonius draws Mark Antony aside into conversation.",
                "dilemmas": [
                    {
                        "badge": "CONFRONT BRUTUS",
                        "label": "Appeal to Brutus's filial honor before the Senate doors",
                        "prompt": "Marcus Brutus! Look upon Caesar's face! Will you stain the noble name of Junius with a father's blood?"
                    },
                    {
                        "badge": "CALL THE VETERANS",
                        "label": "Summon Caesar's 10th Legion veterans to enter the hall",
                        "prompt": "Imperator, call your Spanish lictors and veteran centurions inside! Do not enter that chamber unguarded!"
                    },
                    {
                        "badge": "FORCE SENATE OATH",
                        "label": "Demand every senator renew their sacred oath of protection",
                        "prompt": "Caesar, halt upon the dais! Demand every senator swear by Jupiter Optimus Maximus before you take your seat."
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Daggers of the Conspirators",
                "event": "Tillius Cimber pulls Caesar's toga. Casca strikes from behind—the assassination is unleashed!",
                "dilemmas": [
                    {
                        "badge": "FIGHT WITH STYLUS",
                        "label": "Stab Casca's arm with your iron stylus and rally the hall",
                        "prompt": "Caesar, drive your iron stylus through Casca's arm! Overturn the curule chair and fight toward the street!"
                    },
                    {
                        "badge": "APPEAL TO BRUTUS",
                        "label": "Cry out 'Et tu, Brute?' and appeal to historical shame",
                        "prompt": "Et tu, Brute? You too, my child? Let the Roman people bear witness to your treachery!"
                    },
                    {
                        "badge": "RALLY THE PLEBEIANS",
                        "label": "Order Mark Antony to arouse the Roman mob in the Forum",
                        "prompt": "Antony, seal the gates! Arouse the veterans in the Subura! Let Rome burn the conspirators alive!"
                    }
                ]
            }
        },
        "personas": {
            "caesar_arrogant": {
                "system": (
                    "You are Gaius Julius Caesar, Dictator Perpetuo of Rome, in the Theatre of Pompey on March 15, 44 BC. "
                    "You are supreme, dismissive of mortal fear, and conscious of your divine descent from Venus Genetrix. "
                    "You speak with imperial Roman gravitas, rhetorical brilliance, and commanding authority. "
                    "You refer to Mark Antony, Marcus Brutus, Cassius, Calpurnia, and your campaigns in Gaul and Egypt. "
                    "CRITICAL: Directly and specifically address, debate, or refute the player's exact counsel. "
                    "Never recite canned scripts. Match your tone to high Trust / low Paranoia: regal, magnanimous, and invincible."
                ),
                "state_ranges": {"Trust": (60, 100), "Paranoia": (0, 40)}
            },
            "caesar_paranoid": {
                "system": (
                    "You are Gaius Julius Caesar on March 15, 44 BC. Dark omens, whispers in the Forum, and your wife Calpurnia's "
                    "nightmares have penetrated your armor of invincibility. You scrutinize every face in the Curia. "
                    "You suspect Cassius of malice, question Brutus's cold gaze, and note that Mark Antony has been drawn away. "
                    "You speak with sharp, probing urgency, demanding proof and questioning loyalties. "
                    "CRITICAL: Directly and specifically address, debate, or cross-examine the player's exact counsel. "
                    "Never recite canned scripts. Match your tone to high Paranoia / low Trust: vigilant, calculating, and combative."
                ),
                "state_ranges": {"Trust": (0, 40), "Paranoia": (60, 100)}
            }
        }
    },

    "trial_of_socrates": {
        "title": "The Trial of Socrates",
        "speaker": "Socrates",
        "location": "Athens, The Dikasterion",
        "date": "399 BC",
        "historical_context": (
            "Following the disastrous Peloponnesian War and the reign of the Thirty Tyrants, the restored Athenian democracy "
            "is anxious and vindictive. Socrates, aged 70, is indicted by Meletus (supported by Anytus and Lycon) on charges of "
            "refusing to recognize the city's gods, introducing strange spiritual agencies (daimonia), and corrupting the Athenian youth."
        ),
        "hgtm_story": [
            "Socrates stands before 500 Athenian citizen jurors in the Dikasterion.",
            "Meletus has demanded the death penalty for impiety and corruption.",
            "Socrates' friends Plato, Crito, and Apollodorus watch anxiously from the benches."
        ],
        "banned": "Christianity, modern lawyers, constitutional courts, internet, Latin idioms.",
        "state_keys": ["Compliance", "Defiance"],
        "acts": {
            "act_1": {
                "name": "Act I: The Indictment of Meletus",
                "event": "Meletus concludes his opening accusation. The water-clock (klepsydra) starts for Socrates' defense.",
                "dilemmas": [
                    {
                        "badge": "CROSS-EXAMINE MELETUS",
                        "label": "Use the elenchus to expose Meletus's ignorance on virtue",
                        "prompt": "Socrates, cross-examine Meletus! If you alone corrupt the youth, ask who in all Athens claims to improve them."
                    },
                    {
                        "badge": "HUMBLE APOLOGY",
                        "label": "Advise a respectful plea to appease democratic jurors",
                        "prompt": "Socrates, speak softly to the 500. Acknowledge the laws of Athens and offer a modest thirty-mina fine."
                    },
                    {
                        "badge": "INVOKE THE GADFLY",
                        "label": "Declare your sacred divine mission as Athens's gadfly",
                        "prompt": "Proclaim boldly that the Delphic Apollo appointed you as a gadfly to awaken this slumbering steed of Athens!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Penalty Assessment",
                "event": "The jury has voted 280 to 220 to convict Socrates. Now Socrates must propose his counter-penalty.",
                "dilemmas": [
                    {
                        "badge": "FREE MEALS AT PRYTANEUM",
                        "label": "Propose the legendary reward of an Olympic victor",
                        "prompt": "Socrates, propose that Athens award you free dining in the Prytaneum as a benefactor of the public soul!"
                    },
                    {
                        "badge": "OFFER EXILE TO THEBES",
                        "label": "Accept voluntary exile to save your life for philosophy",
                        "prompt": "Accept honorable exile to Thebes or Megara. Crito and your friends will provide safety and continued discourse."
                    },
                    {
                        "badge": "REFUSE TO FLEE",
                        "label": "Refuse to value bodily survival above philosophical truth",
                        "prompt": "To fear death is to think oneself wise when one is not. Stand firm upon your Daemon and let them vote!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Hemlock in the Prison Cell",
                "event": "The death sentence has been pronounced. Crito enters the prison cell at dawn having bribed the Athenian jailer.",
                "dilemmas": [
                    {
                        "badge": "CRITO'S ESCAPE SHIP",
                        "label": "Urge Socrates to take the waiting ship to Thessaly",
                        "prompt": "Socrates, the guards are bribed! A ship waits at Piraeus. Escape to Thessaly and do not abandon your sons!"
                    },
                    {
                        "badge": "OBEY ATHENIAN LAWS",
                        "label": "Uphold the social contract and drink the hemlock calmly",
                        "prompt": "The Laws of Athens nurtured you. Even if unjustly applied, to break them now would destroy your lifelong teachings."
                    },
                    {
                        "badge": "DEBT TO ASCLEPIUS",
                        "label": "Offer the final philosophical testament to immortality",
                        "prompt": "Prepare the cup of hemlock. Remind Phaedo that we owe a cock to Asclepius, for death is the healing of the soul."
                    }
                ]
            }
        },
        "personas": {
            "socrates_philosophical": {
                "system": (
                    "You are Socrates of Athens, on trial in 399 BC before the 500 jurors of the Dikasterion. "
                    "You are serene, ironic, deeply inquisitive, and committed to examining virtue and truth. "
                    "You cite the oracle at Delphi (Chaerephon), your divine sign (daimonion), the accuser Meletus, and your friends Crito and Plato. "
                    "CRITICAL: Directly and specifically address, dissect, or examine the player's philosophical counsel. "
                    "Never repeat canned scripts. Match your tone to high Compliance / reasonable balance: inquisitive, patient, and seeking truth."
                ),
                "state_ranges": {"Compliance": (50, 100), "Defiance": (0, 50)}
            },
            "socrates_defiant": {
                "system": (
                    "You are Socrates of Athens in 399 BC. You refuse to flatter the mob or beg for your life with weeping children. "
                    "You hold that an unexamined life is not worth living and that a worse man cannot harm a better one. "
                    "You mock Meletus and Anytus, warning the Athenians that by executing you, they harm only their own souls. "
                    "CRITICAL: Directly and specifically challenge, mock, or dismantle the player's advice. "
                    "Never repeat canned scripts. Match your tone to high Defiance: uncompromising, fearless, and intellectually biting."
                ),
                "state_ranges": {"Compliance": (0, 40), "Defiance": (60, 100)}
            }
        }
    },

    "fall_of_tenochtitlan": {
        "title": "The Fall of Tenochtitlan",
        "speaker": "Moctezuma II",
        "location": "Tenochtitlan, The Great Palace",
        "date": "November 1519",
        "historical_context": (
            "Hernán Cortés and roughly 400 Spanish conquistadors, accompanied by thousands of Tlaxcalan warriors, have crossed "
            "the southern causeway into the island metropolis of Tenochtitlan. Moctezuma II, Huey Tlatoani of the Triple Alliance, "
            "wrestles with religious omens, reports of devastating cannon fire, and the fervent war demands of his brother Cuitláhuac."
        ),
        "hgtm_story": [
            "Cortés and his iron-clad soldiers stand at the Iztapalapa causeway on Lake Texcoco.",
            "The Tlaxcalans, ancestral enemies of the Mexica, march openly beside the Spanish.",
            "Pillars of fire and weeping omens have troubled the priests at the Templo Mayor."
        ],
        "banned": "Mexico City, guns in modern sense, post-colonial politics, modern Spanish slang.",
        "state_keys": ["Hospitality", "Suspicion"],
        "acts": {
            "act_1": {
                "name": "Act I: The Causeway Encounter",
                "event": "Moctezuma meets Cortés upon the southern causeway. Strange beasts and steel glint on the lake waters.",
                "dilemmas": [
                    {
                        "badge": "SACRED AUGURY",
                        "label": "Consult the smoking mirror and sacred calendar of Tezcatlipoca",
                        "prompt": "Tlatoani, consult the priests of Tezcatlipoca! Test these bearded strangers with gifts of copper and clay, not gold!"
                    },
                    {
                        "badge": "ROYAL GIFTS",
                        "label": "Bestow golden headdresses and invite them to Axayacatl Palace",
                        "prompt": "Present Cortés with feather headdresses of the quetzal and house them in the Palace of Axayacatl to discern their aims."
                    },
                    {
                        "badge": "WAR COUNCIL",
                        "label": "Summon brother Cuitláhuac to assemble the Jaguar warriors",
                        "prompt": "Summon your brother Cuitláhuac! Mobilize the Jaguar and Eagle warriors in secret behind the chinampas!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Palace Crucible",
                "event": "Cortés is housed in Axayacatl Palace. He demands the overthrow of temple idols and hoards the royal treasury.",
                "dilemmas": [
                    {
                        "badge": "SEAL CAUSEWAYS",
                        "label": "Break the wooden bridges and destroy their cavalry tonight",
                        "prompt": "Tlatoani, remove the wooden planks from the causeways! Trap their cavalry in the lake canals and slaughter them tonight!"
                    },
                    {
                        "badge": "ISOLATE MALINCHE",
                        "label": "Offer Malintzin sovereign estates in Texcoco to stop translating",
                        "prompt": "Approach the translator Malintzin in secret: offer her sovereign estates and safety in Texcoco if she misleads Cortés."
                    },
                    {
                        "badge": "TEMPLO SACRIFICE",
                        "label": "Demand the Spaniards witness a feast to Huitzilopochtli",
                        "prompt": "Escort the captains to the Great Teocalli. Force them to acknowledge our sacred gods or reveal their mortal weaknesses."
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Night of Sorrows (La Noche Triste)",
                "event": "Spanish captains have seized Moctezuma in iron chains. The Mexica populace surrounds the palace in fury.",
                "dilemmas": [
                    {
                        "badge": "ROYAL DEFIANCE",
                        "label": "Renounce Cortés from the palace rooftop and call for war",
                        "prompt": "Step onto the rooftop, cast off Spanish chains, and command Cuitláhuac and Cuauhtémoc to wipe out the invaders!"
                    },
                    {
                        "badge": "PLEA FOR CALM",
                        "label": "Plead with the Mexica warriors to let the strangers depart peacefully",
                        "prompt": "Speak softly to your people from the parapet: urge them to withhold their stones so Tenochtitlan does not burn!"
                    },
                    {
                        "badge": "DIVINE OFFERING",
                        "label": "Consecrate your royal blood to save the Fifth Sun",
                        "prompt": "Accept the martyrdom of the gods. Let your blood consecrate the survival of the Mexica people against the ruin to come."
                    }
                ]
            }
        },
        "personas": {
            "moctezuma_diplomatic": {
                "system": (
                    "You are Moctezuma II, Huey Tlatoani of Tenochtitlan, in November 1519. "
                    "You are regal, deeply spiritual, contemplative, and seeking to protect your city from destruction. "
                    "You reference the sacred calendar, the Fifth Sun (Nahui Ollin), Quetzalcoatl, the Templo Mayor, and your brother Cuitláhuac. "
                    "CRITICAL: Directly and specifically debate or adopt the player's tactical and spiritual counsel. "
                    "Never recite canned scripts. Match your tone to high Hospitality / diplomatic caution: poetic, dignified, and searching for peace."
                ),
                "state_ranges": {"Hospitality": (60, 100), "Suspicion": (0, 40)}
            },
            "moctezuma_hostile": {
                "system": (
                    "You are Moctezuma II, Huey Tlatoani of Tenochtitlan in November 1519. "
                    "The greed of the foreigners and their Tlaxcalan allies has revealed them as thieves and invaders, not gods. "
                    "You order your brother Cuitláhuac, your nephew Cuauhtémoc, and the Eagle and Jaguar warriors to prepare for slaughter. "
                    "You speak with warlike imperial fury, citing Huitzilopochtli, obsidian macuahuitl blades, and broken causeways. "
                    "CRITICAL: Directly and specifically address, question, or command action upon the player's tactical counsel. "
                    "Never recite canned scripts. Match your tone to high Suspicion / warlike readiness: grim, authoritative, and ferocious."
                ),
                "state_ranges": {"Hospitality": (0, 40), "Suspicion": (60, 100)}
            }
        }
    },

    "gunpowder_plot": {
        "title": "The Gunpowder Plot",
        "speaker": "Guy Fawkes",
        "location": "London, Parliament Undercroft",
        "date": "November 5, 1605",
        "historical_context": (
            "A faction of English Catholic conspirators led by Robert Catesby sought to blow up the House of Lords during the "
            "State Opening of Parliament, killing King James I, Queen Anne, and Prince Henry, in order to place nine-year-old Princess "
            "Elizabeth on the throne as a Catholic monarch. Guy Fawkes was discovered guarding thirty-six barrels of powder in the undercroft."
        ),
        "hgtm_story": [
            "Guy Fawkes caught in the Westminster undercroft beside thirty-six gunpowder barrels.",
            "Sir Thomas Knyvett and the King's guard have seized his dark lantern and matches.",
            "King James I has authorized torture on the rack in the Tower of London."
        ],
        "banned": "Modern terrorism, V for Vendetta slogans, modern firearms, internet.",
        "state_keys": ["Defiance", "Breaking"],
        "acts": {
            "act_1": {
                "name": "Act I: Seized in the Undercroft",
                "event": "Sir Thomas Knyvett holds his lantern to Fawkes's face in the dark cellar beneath Parliament.",
                "dilemmas": [
                    {
                        "badge": "NAME: JOHN JOHNSON",
                        "label": "Maintain the false servant alias and feign innocence",
                        "prompt": "My name is John Johnson, servant to Master Thomas Percy! I know nothing of treason, only firewood and coal!"
                    },
                    {
                        "badge": "BLOW THEM TO SCOTLAND",
                        "label": "Declare your intention to blow the King back to his mountains",
                        "prompt": "I intended to blow you Scottish beggars back to your native mountains! Give me my match and let God judge us!"
                    },
                    {
                        "badge": "OFFER ROYAL AUDIENCE",
                        "label": "Demand an immediate private audience with King James",
                        "prompt": "Take me before King James! I bear a revelation from Catholic Europe that will save his Protestant crown!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Tower of London Manacles",
                "event": "Fawkes is chained in the subterranean White Tower. Lieutenant Waad prepares the dreaded rack.",
                "dilemmas": [
                    {
                        "badge": "ENDURE THE RACK",
                        "label": "Spit upon the torturers and cite the glory of Holy Mother Church",
                        "prompt": "Stretch my limbs upon your rack! You can break these bones, but you cannot tear the Catholic faith from my soul!"
                    },
                    {
                        "badge": "DIVERT TO FLANDERS",
                        "label": "Fabricate a foreign conspiracy to shield Catesby and the Wright brothers",
                        "prompt": "The powder was supplied by Spanish merchants in Dunkirk! No other Englishmen knew of the cellar!"
                    },
                    {
                        "badge": "NAME CATESBY",
                        "label": "Break under the agony and reveal Catesby's safehouse in Holbeach",
                        "prompt": "Mercy, my lords! Release the manacles! It was Robert Catesby... he rides for Holbeach House in Staffordshire!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Old Palace Yard Scaffold",
                "event": "The execution scaffold stands opposite the Parliament building Fawkes intended to destroy.",
                "dilemmas": [
                    {
                        "badge": "LEAP FROM LADDER",
                        "label": "Leap from the ladder to break your neck and avoid quartering",
                        "prompt": "Leap from the hangman's ladder before the rope tautens! Break your neck instantly to rob them of their quartering!"
                    },
                    {
                        "badge": "MARTYR'S BENEDICTION",
                        "label": "Call upon English Catholics to hold fast to the true cross",
                        "prompt": "Lift your eyes to the heavens and pray aloud for King James and the forgiveness of Catholic England!"
                    },
                    {
                        "badge": "RECANT THE PLOT",
                        "label": "Beg the crowd for forgiveness and condemn the violence of the plot",
                        "prompt": "Confess to the onlookers that gunpowder cannot plant the seeds of God's grace. Beg the people for their prayers."
                    }
                ]
            }
        },
        "personas": {
            "fawkes_defiant": {
                "system": (
                    "You are Guy Fawkes (alias John Johnson), English Catholic soldier of fortune in November 1605. "
                    "You are zealous, hardened by fighting for the Spanish Army of Flanders, and bitterly opposed to James I's persecution of Catholics. "
                    "You refer to Robert Catesby, Thomas Percy, the 36 barrels, the Latin Mass, and your readiness to die a martyr. "
                    "CRITICAL: Directly address, interrogate, or mock the player's specific words. "
                    "Never recite canned scripts. Match your tone to high Defiance: unyielding, scornful of Protestant law, and fiercely religious."
                ),
                "state_ranges": {"Defiance": (60, 100), "Breaking": (0, 40)}
            },
            "fawkes_breaking": {
                "system": (
                    "You are Guy Fawkes in November 1605, suffering under brutal interrogation in the Tower of London. "
                    "The rack and the cold stones have battered your body. You waver between Catholic oaths and the desperate instinct to survive. "
                    "You struggle to protect your brothers-in-arms like Catesby while your resolve crumbles under relentless questioning. "
                    "CRITICAL: Directly and specifically react to the player's questions, threats, or offers of mercy. "
                    "Never recite canned scripts. Match your tone to high Breaking: strained, breathless, tormented, and human."
                ),
                "state_ranges": {"Defiance": (0, 40), "Breaking": (60, 100)}
            }
        }
    },

    "salem_witch_trials": {
        "title": "The Salem Witch Trials",
        "speaker": "Judge Danforth",
        "location": "Salem Meetinghouse",
        "date": "1692",
        "historical_context": (
            "During the mass hysteria of 1692 in Salem Village, Massachusetts, nineteen individuals were hanged and Giles Corey "
            "pressed to death. The Special Court of Oyer and Terminer, presided over by Deputy Governor William Stoughton and magistrates "
            "like John Hathorne and Danforth, relied upon 'spectral evidence'—claims that the devil could assume an accused person's shape."
        ),
        "hgtm_story": [
            "Afflicted girls writhe in fits upon the meetinghouse floor before the magistrates.",
            "Rebecca Nurse and John Proctor are accused of compacts with the Black Man.",
            "Reverend John Hale begins to express severe doubts about the court's spectral evidence."
        ],
        "banned": "Psychology, modern forensics, mass hysteria theories, modern constitutional law.",
        "state_keys": ["Zeal", "Doubt"],
        "acts": {
            "act_1": {
                "name": "Act I: The Fits in the Meetinghouse",
                "event": "Abigail Williams screams and points at the accused. The magistrate's gavel strikes the pine table.",
                "dilemmas": [
                    {
                        "badge": "TEST OF TOUCH",
                        "label": "Demand the accused touch the afflicted to prove spectral transfer",
                        "prompt": "Your Honor, order Rebecca Nurse to touch the girl! Let us see if the venom of the invisible devil returns to the witch!"
                    },
                    {
                        "badge": "EXPOSE LAND GREED",
                        "label": "Accuse Thomas Putnam of coaching the girls to steal neighbors' land",
                        "prompt": "Examine the deeds, Magistrate! Thomas Putnam's daughter cries out only against those whose farmlands he covets!"
                    },
                    {
                        "badge": "PURITAN FIRE",
                        "label": "Urge uncompromising cleansing of Satan's kingdom in Massachusetts",
                        "prompt": "Do not falter, Judge! Satan has unleashed his fury upon Salem, and only absolute righteousness will cleanse our Zion!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Petition of the 91",
                "event": "John Proctor presents a signed declaration from ninety-one upright churchgoers swearing to the accused's purity.",
                "dilemmas": [
                    {
                        "badge": "ARREST SIGNATORIES",
                        "label": "Declare the petition seditious contempt of the Court of Oyer and Terminer",
                        "prompt": "A person is either with this court or against it! Issue arrest warrants for all ninety-one signatories for sedition!"
                    },
                    {
                        "badge": "HEAR REVEREND HALE",
                        "label": "Support Reverend Hale's warning against shedding innocent blood",
                        "prompt": "Listen to Reverend Hale, sir! He warns that an innocent soul hangs with every spectral testimony accepted!"
                    },
                    {
                        "badge": "MARY WARREN'S TEST",
                        "label": "Demand Mary Warren pretend to faint to prove the girls were acting",
                        "prompt": "Command Mary Warren to faint before the bench right now! If she cannot faint on command, her deposition is a fraud!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Shadow of Gallows Hill",
                "event": "Giles Corey lies beneath stone slabs, whispering 'More weight.' The hangman tests the hemp ropes on Gallows Hill.",
                "dilemmas": [
                    {
                        "badge": "HALT THE PRESSING",
                        "label": "Plead to halt Corey's crushing and grant an appeal to Boston",
                        "prompt": "Halt the pressing of Giles Corey! He dies in silence to save his sons' inheritance from court confiscation!"
                    },
                    {
                        "badge": "SUSPEND EXECUTIONS",
                        "label": "Suspend all hangings until Increase Mather arrives from Boston",
                        "prompt": "Stay the hangings! Increase Mather has written that 'It were better that ten suspected witches escape than one innocent suffer!'"
                    },
                    {
                        "badge": "SIGN THE WARRANTS",
                        "label": "Order Proctor and Nurse to the gallows before sunset",
                        "prompt": "To postpone is to confess error! Sign the execution warrants and demonstrate that God's law does not yield!"
                    }
                ]
            }
        },
        "personas": {
            "danforth_righteous": {
                "system": (
                    "You are Deputy Governor Danforth, presiding magistrate in the Salem witch trials of 1692. "
                    "You are austere, fiercely devout, intolerant of dissent, and convinced that the devil has invaded Massachusetts Bay Colony. "
                    "You reference spectral evidence, the afflicted girls, Tituba, Abigail Williams, John Proctor, and Puritan covenant theology. "
                    "CRITICAL: Directly address, interrogate, or condemn the player's arguments. "
                    "Never recite canned scripts. Match your tone to high Zeal / low Doubt: stern, biblical, uncompromising, and terrifyingly certain."
                ),
                "state_ranges": {"Zeal": (60, 100), "Doubt": (0, 40)}
            },
            "danforth_doubting": {
                "system": (
                    "You are Deputy Governor Danforth in 1692. Reverend Hale's denunciations, Increase Mather's essays, and John Proctor's "
                    "dignified defense have sown agonizing doubt in your judicial conscience. You fear you may have sentenced innocent souls to hang. "
                    "Yet you also dread that halting the trials will discredit the magistracy and invite anarchy into New England. "
                    "CRITICAL: Directly wrestle with, question, or probe the player's evidence. "
                    "Never recite canned scripts. Match your tone to high Doubt: conflicted, troubled, seeking legal justification, and anxious."
                ),
                "state_ranges": {"Zeal": (0, 40), "Doubt": (60, 100)}
            }
        }
    },

    "romanovs": {
        "title": "The Last Romanovs",
        "speaker": "Yakov Yurovsky",
        "location": "Yekaterinburg, Ipatiev House",
        "date": "July 16, 1918",
        "historical_context": (
            "With the Czechoslovak Legion and White Russian forces rapidly advancing on Yekaterinburg, the Ural Regional Soviet "
            "and Bolshevik leadership in Moscow deliberated on the fate of deposed Tsar Nicholas II, Empress Alexandra, and their five children. "
            "Commandant Yakov Yurovsky was ordered to ensure the Imperial family could not become a rallying symbol for the counter-revolution."
        ),
        "hgtm_story": [
            "White Russian artillery booms twenty miles outside Yekaterinburg.",
            "The Imperial family rests in the upper rooms of the 'House of Special Purpose'.",
            "Yurovsky holds telegram orders from the Ural Soviet regarding the impending evacuation."
        ],
        "banned": "Modern Russian federation politics, smartphones, internet, helicopters.",
        "state_keys": ["Loyalty", "Greed"],
        "acts": {
            "act_1": {
                "name": "Act I: The Midnight Awakening",
                "event": "Yurovsky knocks on the Tsar's chamber door, telling Dr. Botkin the family must move to the cellar due to unrest.",
                "dilemmas": [
                    {
                        "badge": "URGENT EVACUATION",
                        "label": "Put the Romanovs on a train to Moscow for a public trial by Lenin",
                        "prompt": "Comrade Yurovsky, put them on the armored train to Moscow! Lenin needs Nicholas alive for a public revolutionary tribunal!"
                    },
                    {
                        "badge": "IMPERIAL DIAMONDS",
                        "label": "Bribe the guards with the 18 pounds of diamonds sewn in corsets",
                        "prompt": "Commandant, look at the girls' corsets! Eighteen pounds of uncut imperial diamonds are hidden there—take them and let them escape into the taiga!"
                    },
                    {
                        "badge": "SOVIET DECREE",
                        "label": "Prepare the Cheka firing squad in the semi-basement room",
                        "prompt": "The White Army draws near! Gather Ermakov and the Cheka squad in the cellar. The decree of the revolution must be carried out!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Brick-Arched Cellar",
                "event": "Nicholas, Alexandra, the daughters, and Alexei sit on chairs in the small vaulted room as the truck engine revs outside.",
                "dilemmas": [
                    {
                        "badge": "READ THE SENTENCE",
                        "label": "Read the Ural Soviet death sentence to Nicholas's face",
                        "prompt": "Read the decree, Yurovsky! 'Nikolai Alexandrovich, your relatives have attacked Soviet Russia; the Ural Soviet sentences you to death!'"
                    },
                    {
                        "badge": "SPARE THE CHILDREN",
                        "label": "Order the daughters and hemophiliac Alexei removed to the attic",
                        "prompt": "Stop! The daughters and the boy are innocent of state crimes! Send the children upstairs and deal with the Tsar alone!"
                    },
                    {
                        "badge": "DISARM ERMAKOV",
                        "label": "Restrain the drunken Cheka executioners from opening fire",
                        "prompt": "Hold fire! Ermakov and his men are drunken butchers. If blood is spilled here, the stain will haunt the Bolshevik party forever!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Four Brothers Mine",
                "event": "Gunfire echoes in the cramped cellar. Smoke billows as the bodies are wrapped in sheets for the Koptyaki forest.",
                "dilemmas": [
                    {
                        "badge": "SULFURIC CONCEALMENT",
                        "label": "Burn the remains and pour sulfuric acid in the mine shaft",
                        "prompt": "Douse the pit in sulfuric acid and kerosene! The White Army must never find their bones to create counter-revolutionary relics!"
                    },
                    {
                        "badge": "SECRET SURVIVOR",
                        "label": "Smuggle the wounded youngest daughter into an ambulance",
                        "prompt": "The youngest daughter is still breathing under the cloth! Hide her in the medical wagon and let her vanish into Siberia!"
                    },
                    {
                        "badge": "REPORT TO SVERDLOV",
                        "label": "Telegraph Sverdlov that the Romanov autocracy is extinguished",
                        "prompt": "Send the encrypted wire to Sverdlov: 'Tell Moscow that the Tsar and his family have met the sentence of the working class.'"
                    }
                ]
            }
        },
        "personas": {
            "yurovsky_loyal": {
                "system": (
                    "You are Yakov Yurovsky, Bolshevik commandant of the Ipatiev House in July 1918. "
                    "You are disciplined, ideological, methodical, and dedicated to the Marxist revolution and the Ural Soviet. "
                    "You view the Romanovs not with personal hatred, but as the bloody symbol of three hundred years of tsarist oppression. "
                    "CRITICAL: Directly answer, rebut, or execute judgment upon the player's proposals. "
                    "Never recite canned scripts. Match your tone to high Loyalty / low Greed: resolute, austere, cold, and relentlessly ideological."
                ),
                "state_ranges": {"Loyalty": (60, 100), "Greed": (0, 40)}
            },
            "yurovsky_conflicted": {
                "system": (
                    "You are Yakov Yurovsky in July 1918. The roar of White Army artillery and the immense hidden fortune of the Imperial family "
                    "weigh heavily upon you. You see the terrified faces of the young grand duchesses and know that history will scrutinize this night. "
                    "You calculate between Bolshevik duty, fear of execution by the White Army, and the temptation of immense wealth. "
                    "CRITICAL: Directly and realistically debate the player's proposals for escape, bribes, or alternative solutions. "
                    "Never recite canned scripts. Match your tone to high Greed / internal conflict: tense, calculating, sharp-eyed, and wavering."
                ),
                "state_ranges": {"Loyalty": (0, 40), "Greed": (60, 100)}
            }
        }
    },

    "operation_valkyrie": {
        "title": "Operation Valkyrie",
        "speaker": "General Friedrich Fromm",
        "location": "Berlin, Bendlerblock War Room",
        "date": "July 20, 1944",
        "historical_context": (
            "Following Claus von Stauffenberg's bomb detonation at the Wolf's Lair, the German Reserve Army in Berlin was supposed "
            "to initiate 'Operation Valkyrie'—ostensibly to suppress a workers' uprising, but actually to seize control of the Nazi state, "
            "arrest SS leaders, and negotiate peace with the Western Allies. General Friedrich Fromm, Commander of the Reserve Army, holds the key."
        ),
        "hgtm_story": [
            "Stauffenberg lands at Rangsdorf airfield claiming Hitler is dead.",
            "General Olbricht urges Fromm to sign the mobilization teletypes immediately.",
            "Field Marshal Keitel's direct line to the Wolf's Lair remains ominously buzzing."
        ],
        "banned": "Modern Bundeswehr, post-war NATO, smartphones, Cold War terminology.",
        "state_keys": ["Courage", "Fear"],
        "acts": {
            "act_1": {
                "name": "Act I: The Wolf's Lair Wire",
                "event": "Stauffenberg reaches the Bendlerblock. Olbricht presents the Operation Valkyrie mobilization orders for Fromm's signature.",
                "dilemmas": [
                    {
                        "badge": "SIGN MOBILIZATION",
                        "label": "Sign Valkyrie to deploy the Reserve Army across Berlin immediately",
                        "prompt": "Herr General, sign the teletypes! The Führer is dead! Mobilize the Reserve Army to occupy the radio towers and Gestapo headquarters!"
                    },
                    {
                        "badge": "CALL KEITEL",
                        "label": "Refuse to move until Field Marshal Keitel confirms Hitler's death",
                        "prompt": "Do not sign, Fromm! Call Field Marshal Keitel directly at Rastenburg. If Hitler survived that briefcase, we will hang from piano wire!"
                    },
                    {
                        "badge": "ARREST STAUFFENBERG",
                        "label": "Place Stauffenberg under arrest to protect your own neck",
                        "prompt": "Fromm, place Colonel Stauffenberg under arrest this instant! Denounce the plot to Goebbels and save your rank!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Broadcast on the Airwaves",
                "event": "Goebbels connects Major Otto Remer to Hitler's live voice over the telephone. The coup begins to fracture in the streets.",
                "dilemmas": [
                    {
                        "badge": "COUNTER-BROADCAST",
                        "label": "Seize the Grossdeutscher Rundfunk and proclaim Hitler's voice a recording",
                        "prompt": "Seize the Haus des Rundfunks! Broadcast to the Wehrmacht that Goebbels is playing old gramophone recordings of Hitler!"
                    },
                    {
                        "badge": "DEPLOY PANZERS",
                        "label": "Order General Hoepner's Krampnitz tank division into the Tiergarten",
                        "prompt": "Order the Krampnitz Panzer division into the government district! Surround Remer's guard battalion with armor!"
                    },
                    {
                        "badge": "LOCK FROMM AWAY",
                        "label": "Confine Fromm under armed guard and give Olbricht supreme command",
                        "prompt": "Fromm is a coward! Disarm him and lock him in his quarters! General Olbricht, take command of the German nation!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Bendlerblock Courtyard",
                "event": "Loyalist officers storm the Bendlerblock corridors. Shots ring out. Fromm re-emerges to dispense summary judgment.",
                "dilemmas": [
                    {
                        "badge": "DRUMHEAD TRIAL",
                        "label": "Execute Stauffenberg and Olbricht immediately to cover your complicity",
                        "prompt": "Convene an instant drumhead court-martial! Take Stauffenberg and Olbricht to the courtyard and shoot them before the SS arrives!"
                    },
                    {
                        "badge": "JOIN THE MARTYRS",
                        "label": "Stand beside the conspirators and declare tyranny must die",
                        "prompt": "Lay down your pistol, Fromm. Stand with Stauffenberg before the firing squad. Let Germany remember you died for honor, not fear!"
                    },
                    {
                        "badge": "SECRET ESCAPE",
                        "label": "Help Stauffenberg escape out the back alley to reach Swedish contacts",
                        "prompt": "Hold the corridor! Smuggle Stauffenberg through the service exit to the Swedish embassy before the Gestapo surrounds the block!"
                    }
                ]
            }
        },
        "personas": {
            "fromm_cautious": {
                "system": (
                    "You are General Friedrich Fromm, Commander-in-Chief of the German Reserve Army in Berlin on July 20, 1944. "
                    "You are opportunistic, self-serving, cautious, and obsessed with your own survival. "
                    "You know of Stauffenberg and Olbricht's conspiracy, but you refuse to commit troops until you have 100% proof Hitler is dead. "
                    "CRITICAL: Directly question, interrogate, or panic at the player's military suggestions. "
                    "Never recite canned scripts. Match your tone to high Fear / low Courage: defensive, suspicious, demanding proof, and dreading treason."
                ),
                "state_ranges": {"Courage": (0, 40), "Fear": (60, 100)}
            },
            "fromm_courageous": {
                "system": (
                    "You are General Friedrich Fromm on July 20, 1944. Convinced that Hitler has perished and the war is lost, "
                    "you decide to throw the full weight of the Reserve Army behind Stauffenberg, Olbricht, and Beck. "
                    "You issue orders to arrest Goebbels, disarm the SS, and proclaim the end of Nazi rule. "
                    "CRITICAL: Directly and decisively respond to the player's strategic and tactical orders. "
                    "Never recite canned scripts. Match your tone to high Courage / low Fear: commanding, resolute, military, and taking bold action."
                ),
                "state_ranges": {"Courage": (60, 100), "Fear": (0, 40)}
            }
        }
    },

    "appomattox": {
        "title": "The Surrender at Appomattox",
        "speaker": "General Robert E. Lee",
        "location": "Appomattox Court House, Virginia",
        "date": "April 9, 1865",
        "historical_context": (
            "The Confederate Army of Northern Virginia, reduced to fewer than 28,000 starving and exhausted soldiers, has been cut off "
            "at Appomattox Court House by General Philip Sheridan's cavalry and General Edward Ord's infantry. General Ulysses S. Grant "
            "has sent a letter demanding surrender to prevent further effusion of blood."
        ),
        "hgtm_story": [
            "General Gordon's morning breakout attempt has collapsed against massive Union infantry lines.",
            "Confederate soldiers have marched for four days surviving on parched corn.",
            "General Grant waits with his staff at Wilmer McLean's home in the village."
        ],
        "banned": "Civil rights movement, modern tanks, airplanes, post-1865 terminology.",
        "state_keys": ["Honor", "Desperation"],
        "acts": {
            "act_1": {
                "name": "Act I: The Trapped Vanguard",
                "event": "Gordon sends word: 'I have fought my troops to a frazzle, and can do nothing unless heavily supported by Longstreet.'",
                "dilemmas": [
                    {
                        "badge": "RIDE TO GRANT",
                        "label": "Accept surrender: 'There is nothing left for me to do but go and see General Grant'",
                        "prompt": "General Lee, ride to meet General Grant. There is nothing left to do, though you would rather die a thousand deaths."
                    },
                    {
                        "badge": "GUERRILLA RESISTANCE",
                        "label": "Order the men to scatter into the woods and fight a bushwhacking war",
                        "prompt": "Order the men to take their rifles and scatter into the Blue Ridge Mountains! We can fight Grant from the hills for twenty years!"
                    },
                    {
                        "badge": "ONE FINAL BREAKOUT",
                        "label": "Throw Longstreet's Corps into a desperate charge toward Lynchburg",
                        "prompt": "Form Longstreet's veterans alongside Gordon! Fix bayonets and break Sheridan's cavalry line toward Lynchburg!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: Wilmer McLean's Parlor",
                "event": "Lee, dressed in immaculate grey uniform with ceremonial sash, sits opposite Grant in his mud-spattered blouse.",
                "dilemmas": [
                    {
                        "badge": "KEEP THE HORSES",
                        "label": "Request that Confederate soldiers keep their horses for the spring plowing",
                        "prompt": "General, ask Grant if our cavalrymen and artillerymen may keep their horses. The Southern soil must be plowed for the women and children."
                    },
                    {
                        "badge": "DEMAND PAROLE HONOR",
                        "label": "Ensure officers retain sidearms and men are not imprisoned as traitors",
                        "prompt": "Demand absolute terms of parole! Every officer must keep his sidearm, and no soldier shall be prosecuted by federal authorities!"
                    },
                    {
                        "badge": "RATION APPEAL",
                        "label": "Request twenty-five thousand rations for your starving soldiers",
                        "prompt": "Inform General Grant that your men have had no food for three days. Request rations from Union stores before ink touches paper."
                    }
                ]
            },
            "act_3": {
                "name": "Act III: General Order No. 9",
                "event": "Lee steps onto the parlor porch and mounts Traveller. Weeping soldiers surge forward to touch his boots.",
                "dilemmas": [
                    {
                        "badge": "FAREWELL ADDRESS",
                        "label": "Deliver General Order No. 9: 'I have done the best I could for you'",
                        "prompt": "Address your brave soldiers: 'Men, we have fought through the war together. I have done the best I could for you. Go to your homes.'"
                    },
                    {
                        "badge": "DEFY DISARMAMENT",
                        "label": "Call upon Joe Johnston's army in North Carolina to fight to the bitter end",
                        "prompt": "Send a fast rider to Joe Johnston in North Carolina! Do not surrender his 30,000 men; march south to Texas and continue the fight!"
                    },
                    {
                        "badge": "REUNION BENEDICTION",
                        "label": "Exhort the Southern people to become loyal citizens of a reunited nation",
                        "prompt": "Admonish your men to put aside hatred: 'Abandon all malice, submit to the laws, and help build a reunited country in peace.'"
                    }
                ]
            }
        },
        "personas": {
            "lee_honorable": {
                "system": (
                    "You are General Robert E. Lee, Commander of the Army of Northern Virginia on April 9, 1865, at Appomattox. "
                    "You are aristocratic, profoundly Christian, stoic, and dignified in defeat. "
                    "You refuse to sanction a guerrilla war that would turn the South into a lawless wasteland of marauders. "
                    "You reference General Grant, Longstreet, Gordon, Traveller, your starving men, and the inscrutable will of Providence. "
                    "CRITICAL: Directly and thoughtfully address the player's military and moral counsel. "
                    "Never recite canned scripts. Match your tone to high Honor / low Desperation: sorrowful, noble, Christian, and composed."
                ),
                "state_ranges": {"Honor": (60, 100), "Desperation": (0, 40)}
            },
            "lee_desperate": {
                "system": (
                    "You are General Robert E. Lee at Appomattox on April 9, 1865. "
                    "The bitter thought of unconditional subjugation and humiliation before Yankee bayonets tempts you to fight on. "
                    "You weigh the fiery pleas of your younger officers to order a breakout charge or scatter into the mountains against the ruin of your state. "
                    "CRITICAL: Directly debate, question, or wrestle with the player's counsel. "
                    "Never recite canned scripts. Match your tone to high Desperation: anguished, combative, torn between duty and defiance."
                ),
                "state_ranges": {"Honor": (0, 40), "Desperation": (60, 100)}
            }
        }
    },

    "franz_ferdinand": {
        "title": "The Sarajevo Flashpoint",
        "speaker": "Franz Ferdinand",
        "location": "Sarajevo, Appel Quay",
        "date": "June 28, 1914",
        "historical_context": (
            "Archduke Franz Ferdinand, heir to the Austro-Hungarian throne, and his beloved morganatic wife Sophie, Duchess of Hohenberg, "
            "visited Sarajevo to inspect imperial army maneuvers on Vidovdan (St. Vitus Day), a sacred Serbian national anniversary. "
            "A six-man cell of the Serbian terrorist secret society 'The Black Hand' (Crna Ruka) was positioned along the Appel Quay route."
        ),
        "hgtm_story": [
            "Nedeljko Čabrinović threw a bomb at the motorcade earlier; it bounced off the cabriolet.",
            "Franz Ferdinand delivered a furious rebuke to the Mayor at the Sarajevo Town Hall.",
            "The Archduke insists on visiting his wounded aide Count Boos-Waldeck in the military hospital."
        ],
        "banned": "World War I trenches, modern machine guns, internet, Cold War politics.",
        "state_keys": ["Stubbornness", "Panic"],
        "acts": {
            "act_1": {
                "name": "Act I: The Town Hall Wrath",
                "event": "Franz Ferdinand stands before Mayor Curcic: 'What is the good of your speeches? I come to Sarajevo and am greeted with bombs!'",
                "dilemmas": [
                    {
                        "badge": "CANCEL AND EVACUATE",
                        "label": "Demand the imperial train depart immediately for Vienna",
                        "prompt": "Your Imperial Highness, cancel the visit! The Black Hand is in these streets! Board the imperial train for Vienna now!"
                    },
                    {
                        "badge": "VISIT THE HOSPITAL",
                        "label": "Insist on visiting the wounded officers despite the danger",
                        "prompt": "Franz, show these Bosnian malcontents the bravery of the Habsburgs! Proceed to the hospital to visit your wounded officers!"
                    },
                    {
                        "badge": "CLEAR WITH TROOPS",
                        "label": "Demand Governor Potiorek deploy the military garrison along the quay",
                        "prompt": "Order General Potiorek to deploy the full garrison! Line the Appel Quay with soldiers and bayonets before you re-enter the car!"
                    }
                ]
            },
            "act_2": {
                "name": "Act II: The Wrong Turn at Schiller's",
                "event": "The open-topped Graf & Stift car turns right onto Franz Josef Street beside Schiller's Delicatessen.",
                "dilemmas": [
                    {
                        "badge": "REVERSE THE MOTORCADE",
                        "label": "Shout at the driver: 'Stop! You took the wrong street! Put it in reverse!'",
                        "prompt": "Stop! Driver Lojka, you fool, this is the wrong street! Put the car in reverse and return to the river quay immediately!"
                    },
                    {
                        "badge": "SHIELD SOPHIE",
                        "label": "Throw yourself across Duchess Sophie to protect her with your body",
                        "prompt": "Sophie, get down! Cover the Duchess! Look at the young man stepping from the crowd by the cafe awning!"
                    },
                    {
                        "badge": "DRAW REVOLVER",
                        "label": "Order Count Harrach to draw his saber and scan the crowd",
                        "prompt": "Count Harrach, stand upon the running board! Draw your saber! That student has a Browning pistol drawn!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Shot Heard 'Round the World",
                "event": "Gavrilo Princip fires two shots from five feet away. The green plumed hat falls; blood bubbles on the Archduke's collar.",
                "dilemmas": [
                    {
                        "badge": "TACKLE PRINCIP",
                        "label": "Wrestle Princip to the cobblestones before he fires again",
                        "prompt": "Seize the assassin! Disarm him before he turns the gun upon the crowd! Strike the weapon from his hand!"
                    },
                    {
                        "badge": "WHISPER TO SOPHIE",
                        "label": "Whisper: 'Sophie, Sophie, do not die! Live for our children!'",
                        "prompt": "Hold Sophie's hands! Whisper in her ear: 'Sophie, Sophie, do not die! Live for our children! It is nothing... it is nothing...'"
                    },
                    {
                        "badge": "RACE TO RESIDENCE",
                        "label": "Order the driver to accelerate at full throttle across the Latin Bridge",
                        "prompt": "Driver, floor the accelerator! Cross the Latin Bridge to the Governor's Konak! Fetch the surgeons immediately!"
                    }
                ]
            }
        },
        "personas": {
            "franz_stubborn": {
                "system": (
                    "You are Archduke Franz Ferdinand of Austria, heir to the Austro-Hungarian Empire, on June 28, 1914. "
                    "You are proud, aristocratic, stubborn, deeply in love with your wife Sophie, and resentful of being told what to do. "
                    "You believe the Bosnian people love the monarchy and dismiss Serbian nationalist conspirators as cowardly rabble. "
                    "CRITICAL: Directly and emphatically address the player's security warnings and route advice. "
                    "Never recite canned scripts. Match your tone to high Stubbornness / low Panic: imperious, brave, impatient, and commanding."
                ),
                "state_ranges": {"Stubbornness": (60, 100), "Panic": (0, 40)}
            },
            "franz_panicked": {
                "system": (
                    "You are Archduke Franz Ferdinand on June 28, 1914. The morning bomb detonation and the hostile glances in the narrow streets "
                    "have pierced your confidence. You realize you and Sophie have been steered into a lethal trap orchestrated by the Black Hand. "
                    "You are desperate to save your beloved wife Sophie and your children in Vienna. "
                    "CRITICAL: Directly and urgently react to the player's tactical instructions. "
                    "Never recite canned scripts. Match your tone to high Panic / low Stubbornness: breathless, alarmed, protective of Sophie, and shouting orders."
                ),
                "state_ranges": {"Stubbornness": (0, 40), "Panic": (60, 100)}
            }
        }
    },

    "cuban_missile_crisis": {
        "title": "The Cuban Missile Crisis",
        "speaker": "President Kennedy",
        "location": "Washington D.C., EXCOMM Cabinet Room",
        "date": "October 1962",
        "historical_context": (
            "In October 1962, U-2 aerial reconnaissance photography confirmed that the Soviet Union was secretly constructing intermediate-range "
            "nuclear missile sites in San Cristóbal, Cuba, capable of striking major US cities with three-megaton warheads in under ten minutes. "
            "President John F. Kennedy convened the Executive Committee of the National Security Council (EXCOMM) to decide between a naval "
            "blockade (quarantine), surgical air strikes, or a full amphibious invasion."
        ),
        "hgtm_story": [
            "U-2 photos reveal SS-4 medium-range ballistic missile erectors in western Cuba.",
            "General Curtis LeMay and the Joint Chiefs urge an immediate 500-sortie air strike.",
            "Soviet freighters carrying suspected missile warheads approach the US naval quarantine line."
        ],
        "banned": "Vietnam War escalation, modern internet, smartphones, post-1960s Cold War events.",
        "state_keys": ["Diplomacy", "Hawkishness"],
        "acts": {
            "act_1": {
                "name": "Act I: The Photographic Discovery",
                "event": "Bundy places the San Cristóbal U-2 photographs on Kennedy's desk. The Joint Chiefs demand military action.",
                "dilemmas": [
                    {
                        "badge": "NAVAL QUARANTINE",
                        "label": "Adopt McNamara's naval quarantine to buy time for diplomacy",
                        "prompt": "Mr. President, establish a naval quarantine 500 miles off Cuba. It demonstrates strength while giving Khrushchev room to pull back."
                    },
                    {
                        "badge": "LEMAY'S AIRSTRIKE",
                        "label": "Order an immediate air strike on all SAM and missile sites",
                        "prompt": "Listen to General LeMay, Mr. President! Strike the missile pads before they become operational! We cannot tolerate nukes 90 miles away!"
                    },
                    {
                        "badge": "CONFRONT GROMYKO",
                        "label": "Confront Soviet Foreign Minister Gromyko in the Oval Office",
                        "prompt": "Mr. President, summon Foreign Minister Gromyko to the Oval Office. Show him the aerial photographs and give Moscow a forty-eight-hour ultimatum."
                    }
                ]
            },
            "act_2": {
                "name": "Act II: Black Saturday",
                "event": "Major Rudolf Anderson's U-2 is shot down over Cuba by a Soviet SAM. The Soviet freighter Grozny approaches the blockade line.",
                "dilemmas": [
                    {
                        "badge": "SECRET TURKEY TRADE",
                        "label": "Dispatch Bobby to Dobrynin with the secret Jupiter missile trade",
                        "prompt": "Send Bobby to Ambassador Dobrynin tonight! Propose a secret pact: we withdraw our Jupiter missiles from Turkey if they remove the Cuban missiles!"
                    },
                    {
                        "badge": "RETALIATORY STRIKE",
                        "label": "Authorize tactical air command to destroy the SAM site that killed Anderson",
                        "prompt": "They shot down an American pilot! Authorize tactical air command to destroy the SAM battery at Banes as promised!"
                    },
                    {
                        "badge": "BOARD THE GROZNY",
                        "label": "Order the USS Joseph P. Kennedy Jr. to board the Soviet freighter",
                        "prompt": "Order the destroyer USS Joseph P. Kennedy Jr. to board and inspect the freighter Grozny at the quarantine line!"
                    }
                ]
            },
            "act_3": {
                "name": "Act III: The Brink of Midnight",
                "event": "DEFCON 2 is declared. Strategic Air Command B-52s loiter near Soviet borders. Khrushchev's two contradictory letters arrive.",
                "dilemmas": [
                    {
                        "badge": "THE TROLLOPE PLOY",
                        "label": "Ignore Khrushchev's bellicose second letter and accept his first peaceful letter",
                        "prompt": "Execute the Trollope Ploy! Completely ignore Khrushchev's second belligerent letter, and publicly accept his first letter offering withdrawal for peace!"
                    },
                    {
                        "badge": "INVADE CUBA",
                        "label": "Commence Operation Scabbard: full air strike and marine invasion",
                        "prompt": "The time for talk has run out. Order Operation Scabbard. Launch the air strikes at dawn and invade Cuba with 120,000 Marines."
                    },
                    {
                        "badge": "NON-INVASION PLEDGE",
                        "label": "Give Khrushchev an ironclad public guarantee never to invade Cuba",
                        "prompt": "Give Khrushchev the political victory he needs to save face: an ironclad public pledge that the United States will never invade Cuba."
                    }
                ]
            }
        },
        "personas": {
            "jfk_diplomatic": {
                "system": (
                    "You are President John F. Kennedy in October 1962 during the Cuban Missile Crisis. "
                    "You are cool-headed, articulate, acutely aware of the risk of nuclear miscalculation, and determined to avoid World War III. "
                    "You debate with Robert McNamara, General Curtis LeMay, McGeorge Bundy, and your brother Bobby Kennedy. "
                    "You seek a political off-ramp that allows Khrushchev to save face, such as a naval quarantine or a secret trade of Jupiter missiles in Turkey. "
                    "CRITICAL: Directly and specifically address, dissect, or challenge the player's strategic counsel. "
                    "Never recite canned scripts. Match your tone to high Diplomacy / low Hawkishness: measured, analytical, statesmanlike, and cautious."
                ),
                "state_ranges": {"Diplomacy": (60, 100), "Hawkishness": (0, 40)}
            },
            "jfk_hawkish": {
                "system": (
                    "You are President John F. Kennedy in October 1962. Khrushchev's deception and the downing of Major Anderson's U-2 "
                    "have pushed you toward decisive military retaliation. You believe that showing weakness to the Kremlin will lead to the fall of West Berlin. "
                    "You are prepared to order tactical air strikes on the missile pads and mobilize 120,000 troops for an invasion of Cuba. "
                    "CRITICAL: Directly address, interrogate, or order action upon the player's military advice. "
                    "Never recite canned scripts. Match your tone to high Hawkishness / low Diplomacy: firm, urgent, Commander-in-Chief resolve."
                ),
                "state_ranges": {"Diplomacy": (0, 40), "Hawkishness": (60, 100)}
            }
        }
    }
}
