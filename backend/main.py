import asyncio
import uvicorn
import importlib
from multiprocessing import Process
from core import session

# Mapping between page values and their corresponding mode modules
MODE_MODULES = {
    "home": "modes.idle",
    "creation": "modes.creation",
    "identify": "modes.identify",
    "hear": "modes.hear",
}

class ModeManager:
    def __init__(self):
        self.current_page = None
        self.mode_task = None

    async def run_mode(self, module_path):
        module = importlib.import_module(module_path)
        if hasattr(module, "run_mode"):
            print(f"[ModeManager] Running mode: {module_path}")
            await module.run_mode()
        else:
            print(f"[ModeManager] Module '{module_path}' has no 'run_mode()'")

    async def monitor_state(self):
        while True:
            if session.state.page != self.current_page:
                print(f"[ModeManager] Page changed to: {session.state.page}")
                self.current_page = session.state.page
                if self.mode_task and not self.mode_task.done():
                    self.mode_task.cancel()
                    try:
                        await self.mode_task
                    except asyncio.CancelledError:
                        print(f"[ModeManager] Previous mode task cancelled.")

                module_path = MODE_MODULES.get(self.current_page)
                if module_path:
                    self.mode_task = asyncio.create_task(self.run_mode(module_path))
                else:
                    print(f"[ModeManager] Unknown mode: {self.current_page}")
            await asyncio.sleep(0.5) 

async def main():
    # Launch Uvicorn in a separate process
    def run_uvicorn():
        uvicorn.run("api:app", host="0.0.0.0", port=8000)

    uvicorn_process = Process(target=run_uvicorn, daemon=True)
    uvicorn_process.start()

    print("[Main] Uvicorn server started.")

    manager = ModeManager()
    try:
        await manager.monitor_state()
    finally:
        uvicorn_process.terminate()
        uvicorn_process.join()
        print("[Main] Uvicorn server stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Main] Shutdown requested via Ctrl+C. Exiting cleanly.")

