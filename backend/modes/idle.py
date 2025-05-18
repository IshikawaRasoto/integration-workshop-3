import asyncio
from core import session

async def run_mode():
    print("[IdleMode] Entered Idle/Home Mode")

    while session.state.page == "home":
        if session.state.accessibility:
            print("Turn on ESP32 Communication") #TODO 
        
        await asyncio.sleep(1)

    print("[IdleMode] Exited Idle/Home Mode")
