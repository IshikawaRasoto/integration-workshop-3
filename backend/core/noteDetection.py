import asyncio
from .utils import *

#Must return the note with its respective duration
async def detect_note_for_column(column_index: int) -> tuple[str, str]:
    await asyncio.sleep(0.050)  # simulate delay

    #TODO really detect 
    note, duration = MELODY1[column_index]          #TODO this should be replaced by a board state
    if duration != "":
        return (note, duration)
    
    note, duration = MELODY1[column_index - 1]      #TODO this should be replaced by a board state
    if duration == "half" or duration == "whole":
        return (note, duration)

    note3, duration3 = MELODY1[column_index - 2]    #TODO this should be replaced by a board state
    note4, duration4 = MELODY1[column_index - 3]    #TODO this should be replaced by a board state

    if duration3 == "whole":
        return (note3, duration3)
    elif duration4 == "whole":
        return(note4,duration4)
    
    return None,""

#Must return all notes with its durations
async def detectBoardNotes() -> list[tuple[str, str]]:
    results = await asyncio.gather(*(detect_note_for_column(i) for i in range(16)))
    return results

#TODO detection of colors
#TODO detection of position
#TODO integrate both