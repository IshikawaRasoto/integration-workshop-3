import asyncio
from core import session

async def run_mode():
    print("[HearMode] Entered Hear Note Mode")

    while session.state.page == "hear":
        # TODO: Play the current note from the melody
        # TODO: Wait for user to place matching note
        # TODO: Use noteDetection to check if it matches

        # TODO: Green LED if correct, advance index
        # TODO: Red LED if incorrect
        # TODO: Yellow LED if nothing detected

        await asyncio.sleep(0.5)  # avoid CPU overuse (this mode doesn't need to be so fast)

    print("[HearMode] Exited Hear Note Mode")
