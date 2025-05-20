import asyncio
import random

#TODO hardcode these notes that I don't know what I am doing.
NOTES = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B", "None"]
DURATIONS = ["quarter", "half", "whole"]  

MOCK_RESULTS = [
    ("C", "quarter"), ("C", "quarter"),
    ("G", "quarter"), ("G", "quarter"),
    ("A", "quarter"), ("A", "quarter"),
    ("G", "half"),
    ("F", "quarter"), ("F", "quarter"),
    ("E", "quarter"), ("E", "quarter"),
    ("D", "quarter"), ("D", "quarter"),
    ("C", "half"),
    ("None", ""), ("None", "")
]

print(f"[NoteDetection] Twinkle Twinkle Board Setup: {MOCK_RESULTS}")

#Must return the note with its respective duration
async def detect_note_for_column(column_index: int) -> tuple[str, str]:
    await asyncio.sleep(0.050)  # simulate delay

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