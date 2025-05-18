import asyncio
from core import session

async def run_mode():
    print("[IdentifyMode] Entered Identify Note Mode")

    while session.state.page == "identify":
        # TODO: Read current note from melody using note_index
        # TODO: Use noteDetection to read placed note
        # TODO: Compare detected note to expected note

        # TODO: Green LED if correct, advance index
        # TODO: Red LED if incorrect
        # TODO: Yellow LED if nothing detected

        
        await asyncio.sleep(0.5) # avoid CPU overuse (this mode doesn't need to be so fast)

    print("[IdentifyMode] Exited Identify Note Mode")
