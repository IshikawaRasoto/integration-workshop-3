import asyncio
from core import session

async def run_mode():
    print("[IdleMode] Entered Idle/Home Mode")
    try:
        while session.state.page == "home":
            session.select_melody(None)
            session.stop_playback()
            if session.state.accessibility:
                print("Turn on ESP32 Communication")  # TODO: esp32 logic
            await asyncio.sleep(1)

    except asyncio.CancelledError: # when ModeManager does .cancel()
        print("[IdleMode] Exited Idle Mode")
        raise
