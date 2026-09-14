/**
 * Historic What-If: Dynamic Narrative Engine
 * Client-Side Application Controller
 */

const API_BASE = 'http://127.0.0.1:8000';

let currentScenarioId = 'ides_of_march';
let scenariosCatalog = [];
let currentGameState = null;

const SCENARIO_THEMES = {
    "ides_of_march": {
        background: "assets/caesar_senate_hall.jpg",
        placeholder: "Advise Caesar, expose conspirators, or alter the fate of Rome...",
        meter1_sub: "Loyalty & Reassurance",
        meter2_sub: "Suspicion & Urgency"
    },
    "trial_of_socrates": {
        background: "assets/socrates_athens_court.jpg",
        placeholder: "Question Socrates, examine virtue, or plea before the 500 Athenians...",
        meter1_sub: "Reason & Compliance",
        meter2_sub: "Defiance & Martyrdom"
    },
    "fall_of_tenochtitlan": {
        background: "assets/tenochtitlan_palace.jpg",
        placeholder: "Counsel Moctezuma, speak of strange omens, or prepare the empire...",
        meter1_sub: "Hospitality & Peace",
        meter2_sub: "Suspicion & War"
    },
    "gunpowder_plot": {
        background: "assets/guy_fawkes_undercroft.jpg",
        placeholder: "Interrogate Guy Fawkes, demand co-conspirators, or ignite the fuse...",
        meter1_sub: "Defiance & Catholic Zeal",
        meter2_sub: "Breaking & Confession"
    },
    "salem_witch_trials": {
        background: "assets/salem_meetinghouse.jpg",
        placeholder: "Address Judge Danforth, question spectral evidence, or save the accused...",
        meter1_sub: "Puritan Zeal",
        meter2_sub: "Doubt & Reason"
    },
    "romanovs": {
        background: "assets/romanov_cellar.jpg",
        placeholder: "Negotiate with Yurovsky, offer safe passage, or enforce the decree...",
        meter1_sub: "Bolshevik Loyalty",
        meter2_sub: "Greed & Bribe"
    },
    "operation_valkyrie": {
        background: "assets/bendlerblock_war_room.jpg",
        placeholder: "Urge General Fromm, issue mobilization orders, or seize Berlin...",
        meter1_sub: "Coup Courage",
        meter2_sub: "Fear & Self-Preservation"
    },
    "appomattox": {
        background: "assets/appomattox_parlor.jpg",
        placeholder: "Counsel General Lee, negotiate honorable parole, or order retreat...",
        meter1_sub: "Honor & Dignity",
        meter2_sub: "Desperation & Guerrilla War"
    },
    "franz_ferdinand": {
        background: "assets/sarajevo_1914.jpg",
        placeholder: "Warn Archduke Franz Ferdinand, change the motorcade route, or cancel the visit...",
        meter1_sub: "Imperial Stubbornness",
        meter2_sub: "Panic & Evasion"
    },
    "cuban_missile_crisis": {
        background: "assets/jfk_war_room.jpg",
        placeholder: "Advise President Kennedy, propose the Turkish missile trade, or hold the quarantine...",
        meter1_sub: "De-escalation & Accord",
        meter2_sub: "Air Strikes & Nuclear Risk"
    }
};

// DOM Elements
const mainViewport = document.getElementById('main-viewport');
const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const thinkingIndicator = document.getElementById('thinking-indicator');
const suggestionsRow = document.getElementById('suggestions-row');
const storyTimeline = document.getElementById('story-timeline');
const scenariosModal = document.getElementById('scenarios-modal');
const scenariosGrid = document.getElementById('scenarios-grid');

// Header Elements
const scenarioTitle = document.getElementById('scenario-title');
const scenarioSubtitle = document.getElementById('scenario-subtitle');
const locationText = document.getElementById('location-text');
const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');
const npcHeaderAvatar = document.getElementById('npc-header-avatar');
const npcHeaderName = document.getElementById('npc-header-name');
const personaBadge = document.getElementById('persona-badge');

// State Meter Elements
const meter1Box = document.getElementById('meter-1-box');
const meter1Name = document.getElementById('meter-1-name');
const meter1Val = document.getElementById('meter-1-val');
const meter1Fill = document.getElementById('meter-1-fill');
const meter1Sub = document.getElementById('meter-1-sub');

const meter2Box = document.getElementById('meter-2-box');
const meter2Name = document.getElementById('meter-2-name');
const meter2Val = document.getElementById('meter-2-val');
const meter2Fill = document.getElementById('meter-2-fill');
const meter2Sub = document.getElementById('meter-2-sub');

// Init
document.addEventListener('DOMContentLoaded', async () => {
    await fetchScenariosCatalog();
    await switchScenario(currentScenarioId);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleSend();
        }
    });
    
    sendBtn.addEventListener('click', () => handleSend());
});

/**
 * Loads the catalog of all 10 historical scenarios
 */
async function fetchScenariosCatalog() {
    try {
        const res = await fetch(`${API_BASE}/scenarios`);
        const data = await res.json();
        scenariosCatalog = data.scenarios || [];
        renderScenariosGrid();
    } catch (err) {
        console.warn("Could not load scenarios from API. Using fallback offline catalog.");
        scenariosCatalog = getFallbackScenarios();
        renderScenariosGrid();
    }
}

/**
 * Switches the active scenario session
 */
async function switchScenario(scenarioId) {
    currentScenarioId = scenarioId;
    closeModal();
    
    // Clear chat
    chatHistory.innerHTML = '';
    
    try {
        const res = await fetch(`${API_BASE}/scenario/start`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ scenario_id: scenarioId })
        });
        const data = await res.json();
        currentGameState = data;
        
        applyScenarioData(data);
    } catch (err) {
        console.error("Error starting scenario:", err);
        applyFallbackScenario(scenarioId);
    }
}

function applyScenarioData(data) {
    const sId = data.scenario_id;
    const theme = SCENARIO_THEMES[sId] || SCENARIO_THEMES["ides_of_march"];

    // Update Viewport Background
    if (mainViewport && theme.background) {
        mainViewport.style.backgroundImage = `url('${theme.background}')`;
    }

    // Header & Meta
    const scTitle = sId.replace(/_/g, ' ').toUpperCase();
    scenarioTitle.innerText = scTitle;
    scenarioSubtitle.innerText = `${data.date} • ${data.location}`;
    locationText.innerText = data.location;
    npcHeaderName.innerText = data.speaker;
    npcHeaderAvatar.innerText = data.speaker.split(' ').pop().charAt(0);
    
    // Progress with Act Title
    updateProgress(data.progress || 10, data.act_name);
    
    // Story So Far
    renderStoryTimeline(data.story_so_far || []);
    
    // State Meters
    updateStateMeters(data.state || {}, theme);
    
    // Active Persona Badge
    updatePersonaBadge(data.active_persona);
    
    // Opening line
    appendNpcMessage(data.speaker, data.opening_line || "What news do you bring?");
    
    // Dynamic placeholder
    userInput.placeholder = theme.placeholder || `Speak with ${data.speaker}, counsel them, or alter history...`;
    
    // Suggestions
    renderSuggestions(data.suggestions || []);
}

function updateProgress(pct, actName) {
    progressFill.style.width = `${pct}%`;
    if (actName) {
        progressText.innerText = `${actName.toUpperCase()} • ${pct}%`;
    } else {
        progressText.innerText = `PROGRESS: ${pct}%`;
    }
}

function updatePersonaBadge(personaName) {
    if (!personaName) return;
    const formatted = personaName.replace(/_/g, ' ').toUpperCase();
    personaBadge.innerText = formatted;
}

function updateStateMeters(stateObj, theme) {
    const keys = Object.keys(stateObj);
    if (keys.length >= 1) {
        const k1 = keys[0];
        const v1 = stateObj[k1];
        meter1Name.innerText = k1.toUpperCase();
        meter1Val.innerText = `${v1}%`;
        meter1Fill.style.width = `${v1}%`;
        if (meter1Sub && theme && theme.meter1_sub) {
            meter1Sub.innerText = theme.meter1_sub;
        }
    }
    if (keys.length >= 2) {
        const k2 = keys[1];
        const v2 = stateObj[k2];
        meter2Name.innerText = k2.toUpperCase();
        meter2Val.innerText = `${v2}%`;
        meter2Fill.style.width = `${v2}%`;
        if (meter2Sub && theme && theme.meter2_sub) {
            meter2Sub.innerText = theme.meter2_sub;
        }
    }
}

function renderStoryTimeline(storyList) {
    storyTimeline.innerHTML = '';
    storyList.forEach((eventText, idx) => {
        const eventEl = document.createElement('div');
        eventEl.className = 'timeline-event';
        
        let actLabel = `Event ${idx + 1}`;
        if (eventText.includes('TIMELINE ESCALATION')) {
            actLabel = '⚡ ACT ESCALATION';
            eventEl.classList.add('act-escalation-event');
        }
        
        eventEl.innerHTML = `
            <div class="timeline-node"></div>
            <div class="timeline-title">${actLabel}</div>
            <div class="timeline-text">${escapeHtml(eventText)}</div>
        `;
        storyTimeline.appendChild(eventEl);
    });
}

function renderSuggestions(suggestions) {
    suggestionsRow.innerHTML = '';
    if (!suggestions || suggestions.length === 0) return;
    suggestions.forEach(item => {
        const btn = document.createElement('button');
        btn.className = 'suggestion-chip';
        const badge = item.badge || item.label || 'TACTICAL';
        const promptText = item.prompt || item.text || '';
        btn.innerHTML = `<span class="chip-badge">${escapeHtml(badge)}</span> <span class="chip-quote">"${escapeHtml(promptText)}"</span>`;
        btn.onclick = () => {
            userInput.value = promptText;
            handleSend();
        };
        suggestionsRow.appendChild(btn);
    });
}

async function handleSend() {
    const text = userInput.value.trim();
    if (!text) return;
    
    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;
    
    // Append player message
    appendPlayerMessage(text);
    
    // Show thinking indicator
    thinkingIndicator.style.display = 'block';
    thinkingIndicator.innerText = `${npcHeaderName.innerText} is weighing your words...`;
    chatHistory.scrollTop = chatHistory.scrollHeight;
    
    try {
        const res = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                prompt: text,
                scenario_id: currentScenarioId
            })
        });
        
        const data = await res.json();
        
        thinkingIndicator.style.display = 'none';
        
        // Show delta toast if deltas exist
        if (data.deltas && Object.keys(data.deltas).length > 0) {
            renderDeltaToast(data.deltas, data.rationale);
        }
        
        // Append NPC response
        appendNpcMessage(data.speaker, data.response);
        
        // Milestone announcement
        if (data.milestone) {
            appendMilestoneCard(data.milestone);
        }
        
        // Update meters & timeline
        const theme = SCENARIO_THEMES[currentScenarioId] || SCENARIO_THEMES["ides_of_march"];
        updateStateMeters(data.state, theme);
        updatePersonaBadge(data.active_persona);
        updateProgress(data.progress, data.act_name);
        renderStoryTimeline(data.story_so_far);
        renderSuggestions(data.suggestions || []);
        
    } catch (err) {
        thinkingIndicator.style.display = 'none';
        appendNpcMessage("System", "Communication with the local engine encountered an issue. Is the API server running?");
        console.error(err);
    } finally {
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

function appendPlayerMessage(text) {
    const now = new Date();
    const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    
    const row = document.createElement('div');
    row.className = 'chat-row player-row';
    row.innerHTML = `
        <div class="bubble-avatar">P</div>
        <div class="bubble-body">
            <div class="bubble-meta">
                <span class="bubble-speaker">PLAYER</span>
                <span class="bubble-time">${timeStr}</span>
            </div>
            <div class="bubble-text">${escapeHtml(text)}</div>
        </div>
    `;
    chatHistory.appendChild(row);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function appendNpcMessage(speaker, text) {
    const now = new Date();
    const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const initial = speaker.split(' ').pop().charAt(0);
    
    const row = document.createElement('div');
    row.className = 'chat-row npc-row';
    row.innerHTML = `
        <div class="bubble-avatar">${initial}</div>
        <div class="bubble-body">
            <div class="bubble-meta">
                <span class="bubble-speaker">${escapeHtml(speaker)}</span>
                <span class="bubble-time">${timeStr}</span>
            </div>
            <div class="bubble-text">${escapeHtml(text)}</div>
        </div>
    `;
    chatHistory.appendChild(row);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function appendMilestoneCard(milestoneText) {
    const card = document.createElement('div');
    const isEscalation = milestoneText.includes('TIMELINE ESCALATION');
    card.className = isEscalation ? 'milestone-announcement milestone-escalation' : 'milestone-announcement';
    const icon = isEscalation ? '⚔️' : '🏛️';
    const label = isEscalation ? 'CRITICAL ESCALATION' : 'TIMELINE DIVERGENCE';
    card.innerHTML = `${icon} <span><strong>${label}:</strong> ${escapeHtml(milestoneText)}</span>`;
    chatHistory.appendChild(card);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function renderDeltaToast(deltas, rationale) {
    const toast = document.createElement('div');
    toast.className = 'delta-toast';
    
    let deltaHTML = '';
    for (const [key, val] of Object.entries(deltas)) {
        if (val !== 0) {
            const sign = val > 0 ? `+${val}` : `${val}`;
            const cls = val > 0 ? 'pos' : 'neg';
            const arrow = val > 0 ? '▲' : '▼';
            deltaHTML += `<span class="delta-item ${cls}">${arrow} ${sign}% ${key}</span>`;
        }
    }
    
    if (deltaHTML) {
        toast.innerHTML = `${deltaHTML} <span class="delta-rationale">(${escapeHtml(rationale)})</span>`;
        chatHistory.appendChild(toast);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
}

/**
 * Modal & Scenarios Grid
 */
function renderScenariosGrid() {
    scenariosGrid.innerHTML = '';
    scenariosCatalog.forEach(sc => {
        const card = document.createElement('div');
        card.className = `scenario-card ${sc.id === currentScenarioId ? 'active-card' : ''}`;
        
        const keysHtml = (sc.state_keys || []).map(k => `<span class="state-key-tag">${escapeHtml(k)}</span>`).join('');
        
        card.innerHTML = `
            <div class="card-era">${escapeHtml(sc.date)}</div>
            <div class="card-title">${escapeHtml(sc.title)}</div>
            <div class="card-location">📍 ${escapeHtml(sc.location)} • ${escapeHtml(sc.speaker)}</div>
            <div class="card-state-keys">${keysHtml}</div>
            <button class="select-scenario-btn">Enter Timeline</button>
        `;
        
        card.onclick = () => switchScenario(sc.id);
        scenariosGrid.appendChild(card);
    });
}

function openModal() {
    renderScenariosGrid();
    scenariosModal.classList.add('open');
}

function closeModal() {
    scenariosModal.classList.remove('open');
}

function resetTimeline() {
    if (confirm("Reset current historical timeline to its initial state?")) {
        switchScenario(currentScenarioId);
    }
}

function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function getFallbackScenarios() {
    return [
        { id: "ides_of_march", title: "The Ides of March", date: "March 15, 44 BC", location: "Rome, Theatre of Pompey", speaker: "Julius Caesar", state_keys: ["Trust", "Paranoia"] },
        { id: "trial_of_socrates", title: "The Trial of Socrates", date: "399 BC", location: "Athens, The Dikasterion", speaker: "Socrates", state_keys: ["Compliance", "Defiance"] },
        { id: "fall_of_tenochtitlan", title: "The Fall of Tenochtitlan", date: "November 1519", location: "Tenochtitlan, Great Palace", speaker: "Moctezuma II", state_keys: ["Hospitality", "Suspicion"] },
        { id: "gunpowder_plot", title: "The Gunpowder Plot", date: "November 5, 1605", location: "London, Parliament Undercroft", speaker: "Guy Fawkes", state_keys: ["Defiance", "Breaking"] },
        { id: "salem_witch_trials", title: "The Salem Witch Trials", date: "1692", location: "Salem Meetinghouse", speaker: "Judge Danforth", state_keys: ["Zeal", "Doubt"] },
        { id: "romanovs", title: "Final Days of the Romanovs", date: "July 1918", location: "Yekaterinburg, Ipatiev House", speaker: "Yakov Yurovsky", state_keys: ["Loyalty", "Greed"] },
        { id: "operation_valkyrie", title: "Operation Valkyrie", date: "July 20, 1944", location: "Berlin, Bendlerblock", speaker: "General Fromm", state_keys: ["Courage", "Fear"] },
        { id: "appomattox", title: "The Surrender at Appomattox", date: "April 9, 1865", location: "Appomattox Court House", speaker: "General Lee", state_keys: ["Honor", "Desperation"] },
        { id: "franz_ferdinand", title: "Assassination of Franz Ferdinand", date: "June 28, 1914", location: "Sarajevo, City Hall", speaker: "Franz Ferdinand", state_keys: ["Stubbornness", "Panic"] },
        { id: "cuban_missile_crisis", title: "The Cuban Missile Crisis", date: "October 1962", location: "Washington D.C., Oval Office", speaker: "President Kennedy", state_keys: ["Diplomacy", "Hawkishness"] }
    ];
}
