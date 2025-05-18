import asyncio
import time
from core import session, hardware, noteDetection

beats = 0
lastColumnIndex = None  
notesIndex = {}

async def run_mode():
    global beats, lastColumnIndex
    start_time = time.time()
    print("[CreationMode] Entered Creation Mode")
    try:
        while session.state.page == "creation":
            if session.state.playing:
                elapsed = time.time() - start_time
                print(f"[Beat {beats}] Elapsed Time: {elapsed:.3f}s")
                
                columnIndex = beats % 16  # 0 to 15

                if lastColumnIndex is not None:
                    hardware.turnOffLed(lastColumnIndex)

                hardware.turnOnLed(columnIndex)  
                lastColumnIndex = columnIndex
                # TODO: Play the note corresponding to the current column, with not updated list

                # TODO: Really Detect the notes
                notes_and_durations = await noteDetection.detectBoardNotes()    #Update it
                # print(f"[CreationMode] Board state: {notes_and_durations}")

                beats += 1

            await asyncio.sleep((60 / session.state.tempo) / 4) 

    except asyncio.CancelledError: # when ModeManager does .cancel()
        if lastColumnIndex is not None:
            hardware.turnOffLed(lastColumnIndex)
            lastColumnIndex = None
        print("[CreationMode] Exited Creation Mode")

