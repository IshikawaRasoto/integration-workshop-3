from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from core import session


def current_state_dict() -> Dict[str, Any]:
    """Return the full state + computed current_note."""
    current_note = "G4" if session.state.melody else None
    return {
        "volume": session.state.volume,
        "tempo": session.state.tempo,
        "playing": session.state.playing,
        "melody": session.state.melody,
        "note_index": session.state.note_index,
        "current_note": current_note,
        "set_page": session.state.page
    }

class ConnectionManager:
    def __init__(self) -> None:
        self.active: List[WebSocket] = []

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self.active.append(ws)
        await ws.send_json({"type": "state", "state": session.as_dict()})

    def disconnect(self, ws: WebSocket) -> None:
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast_state(self) -> None:
        message = {"type": "state", "state": session.as_dict()}
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

frontend_root = Path(__file__).parents[1] / "interface-web"
app.mount("/static", StaticFiles(directory=frontend_root, html=False), name="static")

# Root endpoint returns the home page
@app.get("/", response_class=HTMLResponse)
async def root():
    file_path = frontend_root / "homePage" / "index.html"
    return file_path.read_text(encoding="utf-8")


# WebSocket route
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)          
    try:
        while True:
            data = await ws.receive_json()
            action = data.get("action")
            value  = data.get("value")

            match action:
                case "set_volume":      session.set_volume(int(value))
                case "set_tempo":       session.set_tempo(int(value))
                case "start":           session.start_playback()
                case "stop":            session.stop_playback()
                case "select_melody":   session.select_melody(str(value))
                case "set_page":        session.set_page(str(value))
                case "set_accessibility": session.set_accessibility(bool(value))
                case _:                 continue            # ignore bad action
            await manager.broadcast_state()                 # notify everyone

    except WebSocketDisconnect:
        manager.disconnect(ws)

    except Exception as e:
        print(f"WebSocket error: {e}")
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
