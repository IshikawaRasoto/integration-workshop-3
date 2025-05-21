import asyncio
from core import session

async def run_mode():
    print("[HearMode] Entered Hear Note Mode")
    try:
        while (session.state.page == "hear"):
            while(session.state.playing and session.state.melody is not None):
                print("loop")
                # TODO: Play the current note from the melody
                # TODO: Wait for user to place matching note
                # TODO: Use noteDetection to check if it matches

                # TODO: Green LED if correct, advance index
                # TODO: Red LED if incorrect
                # TODO: Yellow LED if nothing detected
                await asyncio.sleep(0.5)  # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)

            await asyncio.sleep(1)  # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)
            
    except asyncio.CancelledError: # when ModeManager does .cancel()
        print("[HearMode] Exited Hear Note Mode")
        raise
