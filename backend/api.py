from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from backend.currentData.session import (
    state, set_volume, set_tempo, start_playback,
    stop_playback, select_melody, set_page, as_dict
)

def current_state_dict() -> Dict[str, Any]:
    """Return the full state + computed current_note."""
    current_note = "G4" if state.melody else None
    return {
        "volume": state.volume,
        "tempo": state.tempo,
        "playing": state.playing,
        "melody": state.melody,
        "note_index": state.note_index,
        "current_note": current_note,
        "set_page": state.page
    }

class ConnectionManager:
    def __init__(self) -> None:
        self.active: List[WebSocket] = []

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self.active.append(ws)
        await ws.send_json({"type": "state", "state": as_dict()})

    def disconnect(self, ws: WebSocket) -> None:
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast_state(self) -> None:
        message = {"type": "state", "state": as_dict()}
        to_remove: List[WebSocket] = []
        for ws in self.active:
            try:
                await ws.send_json(message)
            except WebSocketDisconnect:
                to_remove.append(ws)
        for ws in to_remove:
            self.disconnect(ws)

manager = ConnectionManager()
app = FastAPI()

# 1. Serve static files (HTML/CSS/JS/images)
frontend_root = Path(__file__).parents[1] / "interface-web"
app.mount("/static", StaticFiles(directory=frontend_root, html=False), name="static")

# 2. Root endpoint returns the home page
@app.get("/", response_class=HTMLResponse)
async def root():
    file_path = frontend_root / "homePage" / "index.html"
    return file_path.read_text(encoding="utf-8")


# 3. WebSocket route
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            data = await ws.receive_json()
            # Expect {"action": "...", "value": ...}
            action = data.get("action")
            value = data.get("value")

            if action == "set_volume":
                set_volume(int(value))
            elif action == "set_tempo":
                set_tempo(int(value))
            elif action == "start":
                start_playback()
            elif action == "stop":
                stop_playback()
            elif action == "select_melody":
                select_melody(str(value))
            elif action == "set_page":      
                set_page(str(value)) 
            else:
                # unknown action 
                pass

            await manager.broadcast_state()

    except (WebSocketDisconnect, RuntimeError):
        manager.disconnect(ws)

@app.get("/creation")
async def creation_redirect():
    return RedirectResponse(url="/static/creationMode/creationMode.html")

@app.get("/hear")
async def hear_redirect():
    return RedirectResponse(url="/static/hearNote/hearNote.html")

@app.get("/identify")
async def identify_redirect():
    return RedirectResponse(url="/static/identifyNote/identifyNote.html")

async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)          
    try:
        while True:
            data = await ws.receive_json()
            action = data.get("action")
            value  = data.get("value")

            match action:
                case "set_volume":      set_volume(int(value))
                case "set_tempo":       set_tempo(int(value))
                case "start":           start_playback()
                case "stop":            stop_playback()
                case "select_melody":   select_melody(str(value))
                case "set_page":        set_page(str(value))
                case _:                 continue            # ignore bad action
            await manager.broadcast_state()                 # notify everyone

    except WebSocketDisconnect:
        manager.disconnect(ws)

    except Exception as e:
        print(f"WebSocket error: {e}")
        manager.disconnect(ws)