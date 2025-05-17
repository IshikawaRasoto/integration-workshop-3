let ws;
let latestState = {};

function connectWS() {
    ws = new WebSocket(`ws://${location.host}/ws`);

    ws.onopen = () => {}; //removed set page home

    ws.onmessage = (ev) => {
        const msg = JSON.parse(ev.data);
        if (msg.type !== "state") return;

        latestState = msg.state;
        applyStateToDOM(msg.state);
        maybeRedirectPage(msg.state);
    };

    ws.onclose = () => setTimeout(connectWS, 1000);   
}

function sendAction(action, value=null) {
    if (ws?.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({action, value}));
    }
}


function applyStateToDOM(s) {
    const v = document.getElementById("volumeDisplay");
    if (v) v.textContent = `🔊 ${s.volume}%`;

    const t = document.getElementById("tempDisplay");
    if (t) t.textContent = `${s.tempo} BPM`;

    const p = document.getElementById("playStatus");
    if (p) p.textContent = s.playing ? "▶️ Playing" : "⏹️ Stopped";

    const m = document.getElementById("musicSelect");
    if (m && s.melody) m.value = s.melody;

    const n = document.getElementById("currentNote");
    if (n && s.current_note) n.textContent = s.current_note;

    const sw = document.getElementById("accessibilityToggle");
    if (sw && typeof s.accessibility === "boolean") sw.checked = s.accessibility;
}

function maybeRedirectPage(s) {
    const current = window.__PAGE_NAME__ || "home";
    if (s.page !== current) {
        // we are on the wrong page, go to the right one
        switch(s.page) {
            case "identify": location.href = "/identify"; break;
            case "hear":     location.href = "/hear";     break;
            case "creation": location.href = "/creation"; break;
            default:         location.href = "/";         break;
        }
    }
}

connectWS();