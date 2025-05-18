import asyncio
from core import session

async def run_mode():
    print("[CreationMode] Entered Creation Mode")

    while session.state.page == "creation":
        if session.state.playing:
            # TODO: Determine the current note from melody
            # TODO: Play the note corresponding to the current column
            # TODO: Update LEDs to indicate current column
            # TODO: Move to next column after a delay based on tempo
            pass

        #TODO adjust time if the above steps take time
        await asyncio.sleep(60 / session.state.tempo)  # Wait based on BPM


    print("[CreationMode] Exited Creation Mode")
