import asyncio
from core import session

async def run_mode():
    print("[IdentifyMode] Entered Identify Note Mode")
    try:
        while session.state.page == "identify":
            while(session.state.playing and session.state.melody is not None):
                print("loop")
                # TODO: Read current note from melody using note_index
                # TODO: Use noteDetection to read placed note
                # TODO: Compare detected note to expected note

                # TODO: Green LED if correct, advance index
                # TODO: Red LED if incorrect
                # TODO: Yellow LED if nothing detected
                await asyncio.sleep(0.5) # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)
            await asyncio.sleep(1) # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)


    except asyncio.CancelledError: # when ModeManager does .cancel()
        print("[IdentifyMode] Exited Identify Note Mode")
        raise
        

