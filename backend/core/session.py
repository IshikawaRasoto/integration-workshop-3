from dataclasses import dataclass
from typing import Optional

from .utils import *
from .soundPlaying import *

@dataclass
class PlayerState:
    volume: int = 50                 # 0‒100  (%)
    tempo: int = 60                  # BPM
    playing: bool = False            # True if currently playing
    page: str = "home"               # Page represents actual state 
    melody: Optional[str] = None     # name / id of the melody
    note: Optional[str] = None       # note within the melody 
    accessibility: bool = False      # True if accessbility is turned on
    note_index: int = 0              # Which note it is (note + duration)

state = PlayerState()

def set_volume(value: int) -> None:
    volume = max(0, min(100, value)) # 0-100

    #TODO  INCREASE VOLUME ON SPEAKER
    state.volume = volume # 0-100
    print(state.volume)

def set_tempo(bpm: int) -> None:
    tempo = max(60, min(120, bpm))
    state.tempo = tempo   # 60,90,120
    print(state.tempo)

def start_playback() -> None:
    state.playing = True
    print(state.playing)

def stop_playback() -> None:
    state.playing = False
    print(state.playing)
    
def select_melody(name: str) -> None:
    state.melody = name
    if name == "Ovelha Preta":
        state.note, _ = OVELHA_PRETA[0]
    else:
        state.note = None
    print(f"On select_melody {state.melody}  {state.note}")

def set_page(name: str) -> None:
    state.page = name 
    print(f"On set_page {state}")

def set_note(note: str) -> None:
    state.note = note 
    print(f"On set_note {state}")

def set_note_index(idx: int) -> None:
    state.note_index = idx 
    print(f"On set_note_index {state}")

def set_accessibility(flag: bool) -> None:        
    state.accessibility = bool(flag)
    print(f"[state] accessibility  {state.accessibility}")

async def play_current_melody_note() -> None:
    if state.note:
        if state.melody == "Ovelha Preta":
            note, duration = OVELHA_PRETA[state.note_index]
        #TODO Two more melodies

        if duration == "quarter":
            await play_note_async(note, 1)
        elif duration == "half":
            await play_note_async(note, 2)
        elif duration == "whole":
            await play_note_async(note,4)


def as_dict() -> dict:
    return {
        "volume"       : state.volume,
        "tempo"        : state.tempo,
        "playing"      : state.playing,
        "page"         : state.page,
        "melody"       : state.melody,
        "note"         : state.note,
        "accessibility": state.accessibility,
        "note_index"   : state.note_index
    }