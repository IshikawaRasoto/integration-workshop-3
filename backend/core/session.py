from dataclasses import dataclass
from typing import Optional

@dataclass
class PlayerState:
    volume: int = 50                 # 0‒100  (%)
    tempo: int = 60                  # BPM
    playing: bool = False            # True if currently playing
    page: str = "home"               # Page represents actual state 
    melody: Optional[str] = None     # name / id of the melody
    note_index: Optional[int] = 0    # position within the melody
    accessibility: bool = False      # True if accessbility is turned on

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
    state.note_index = 0
    print(state)

def set_page(name: str) -> None:
    state.page = name 
    print(f"On set_page {state}")

def set_accessibility(flag: bool) -> None:        
    state.accessibility = bool(flag)
    print(f"[state] accessibility → {state.accessibility}")

def as_dict() -> dict:
    current_note = "G4" if state.melody else None
    return {
        "volume"      : state.volume,
        "tempo"       : state.tempo,
        "playing"     : state.playing,
        "page"        : state.page,
        "melody"      : state.melody,
        "note_index"  : state.note_index,
        "current_note": current_note,
        "accessibility": state.accessibility,
    }