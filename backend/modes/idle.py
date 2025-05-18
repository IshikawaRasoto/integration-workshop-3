import asyncio
from core import session

async def run_mode():
    print("[IdleMode] Entered Idle/Home Mode")
    try:
        while session.state.page == "home":
            if session.state.accessibility:
                print("Turn on ESP32 Communication")  # TODO: esp32 logic
            await asyncio.sleep(1)
        print("[IdleMode] Detected page-change in loop")

    except asyncio.CancelledError: # when ModeManager does .cancel()
        print("[IdleMode] Task was cancelled")
        raise
    finally:
        print("[IdleMode] Exited Idle Mode")
