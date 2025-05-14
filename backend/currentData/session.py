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

state = PlayerState()

def set_volume(value: int) -> None:
    state.volume = max(0, min(100, value)) # 0-100

def set_tempo(bpm: int) -> None:
    state.tempo = max(60, min(120, bpm))   # 60,90,120

def start_playback() -> None:
    state.playing = True

def stop_playback() -> None:
    state.playing = False

def select_melody(name: str) -> None:
    state.melody = name
    state.note_index = 0

def set_page(name: str) -> None:
    state.page = name 