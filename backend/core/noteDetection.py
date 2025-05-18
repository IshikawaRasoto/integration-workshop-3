import asyncio
import random

#TODO hardcode these notes that I don't know what I am doing.
NOTES = ["C4", "C#4", "Db4", "D4", "D#4", "Eb4", "E4", "F4", "F#4", "Gb4", "G4", "G#4", "Ab4", "A4", "A#4", "Bb4", "B4", "None"]
DURATIONS = ["quarter", "half", "whole"]  

MOCK_RESULTS = []
for i in range(16):
    note = random.choice(NOTES)
    duration = random.choice(DURATIONS) if note != "None" else ""
    MOCK_RESULTS.append((note, duration))
print(f"[NoteDetection] Mocked Board Setup: {MOCK_RESULTS}")

#Must return the note with its respective duration
async def detect_note_for_column(column_index: int) -> tuple[str, str]:
    await asyncio.sleep(0.005)  # simulate delay

    #TODO really detect 
    note, duration = MOCK_RESULTS[column_index]
    # print(f"[NoteDetection] Column {column_index}: {note}, {duration}")
    return (note, duration)

#Must return all notes with its durations
async def detectBoardNotes() -> list[tuple[str, str]]:
    results = await asyncio.gather(*(detect_note_for_column(i) for i in range(16)))
    # print(f"[NoteDetection] Board Detected: {results}")
    return results

#TODO detection of colors
#TODO detection of position
#TODO integrate both