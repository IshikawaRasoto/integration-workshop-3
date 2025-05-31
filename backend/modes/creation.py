import asyncio
import time
import sounddevice as sd
from core import detectionThread
from core import session, hardware, soundPlaying
from core.utils import *
from core.detectionThread import NoteDetection

beats = 0
lastColumnIndex = None  
detect_task = None

async def run_mode():
    thread =  NoteDetection()
    global beats, lastColumnIndex
    start_time = time.time()

    print("[CreationMode] Entered Creation Mode")
    try:
        while session.state.page == "creation":

            notes_and_durations = thread.get_notes_detected()

            if session.state.playing:

                elapsed = time.time() - start_time
                print(f"[Beat {beats}] Elapsed Time: {elapsed:.3f}s")#for debuggin tempo
                
                columnIndex = beats % 16  # 0 to 15

                if lastColumnIndex is not None:
                    hardware.turnOffLed(lastColumnIndex)
                
                if columnIndex == 0 and beats != 0:
                    await asyncio.sleep(1.5)  #little delay to start again

                hardware.turnOnLed(columnIndex)  
                lastColumnIndex = columnIndex
                
                note, duration = notes_and_durations[columnIndex]
                _, duration1 = notes_and_durations[columnIndex - 1]
                _, duration2 = notes_and_durations[columnIndex - 2]
                _, duration3 = notes_and_durations[columnIndex - 3]

                durationInt = get_duration_value(duration)

                if note == "R":
                    if (duration1 == "half" or duration1 == "whole" or
                       duration2 == "whole" or duration3 == "whole"):
                        beats += 1
                        await asyncio.sleep((60 / session.state.tempo)) 
                        continue    
                    else:
                        sd.stop()
                else:
                    await soundPlaying.play_note_async(note,(60 / session.state.tempo) * durationInt)

                beats += 1

            await asyncio.sleep((60 / session.state.tempo)) 

    except asyncio.CancelledError: # when ModeManager does .cancel()
        if lastColumnIndex is not None:
            hardware.turnOffLed(lastColumnIndex)
            lastColumnIndex = None
        print("[CreationMode] Exited Creation Mode")

def get_empty_board():
    return [("None", "") for _ in range(16)]

def get_duration_value(duration_string):
    if(duration_string == "quarter"):
        return 1
    elif(duration_string == "half"):
        return 2
    elif(duration_string == "whole"):
        return 4