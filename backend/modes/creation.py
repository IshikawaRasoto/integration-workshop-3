import asyncio
import time
import sounddevice as sd
from core import session, hardware, noteDetection, soundPlaying

beats = 0
lastColumnIndex = None  

async def run_mode():
    global beats, lastColumnIndex
    start_time = time.time()
    notes_and_durations = get_empty_board()
    detect_task = None
    print("[CreationMode] Entered Creation Mode")
    try:
        while session.state.page == "creation":
            if session.state.playing:

                if detect_task is not None and detect_task.done():
                    notes_and_durations = detect_task.result()

                # TODO: Really Detect the notes
                detect_task = asyncio.create_task(noteDetection.detectBoardNotes())

                elapsed = time.time() - start_time
                print(f"[Beat {beats}] Elapsed Time: {elapsed:.3f}s")
                
                columnIndex = beats % 16  # 0 to 15

                if lastColumnIndex is not None:
                    hardware.turnOffLed(lastColumnIndex)

                hardware.turnOnLed(columnIndex)  
                lastColumnIndex = columnIndex
                
                # TODO: Play the note corresponding to the current column, with not updated list
                note = notes_and_durations[columnIndex][0]
                if note == "None":
                    sd.stop()
                else:
                    await soundPlaying.play_note_async(note,(60 / session.state.tempo) / 4)

                # print(f"[CreationMode] Board state: {notes_and_durations}")

                beats += 1

            await asyncio.sleep((60 / session.state.tempo)) 

    except asyncio.CancelledError: # when ModeManager does .cancel()
        if lastColumnIndex is not None:
            hardware.turnOffLed(lastColumnIndex)
            lastColumnIndex = None
        print("[CreationMode] Exited Creation Mode")

def get_empty_board():
    return [("None", "") for _ in range(16)]