#TODO hardcode melodies (sequence of notes with duration)

MELODY1 = [
    ("G", "quarter"), ("G", "quarter"), ("D", "quarter"), ("D", "quarter"),
    ("E", "quarter"), ("E", "quarter"), ("D", "half"),    ("None", ""),
    ("C", "quarter"), ("C", "quarter"), ("B", "quarter"), ("B", "quarter"),
    ("A", "quarter"), ("A", "quarter"), ("G", "half"),    ("None", "")
]

#TODO hardcode notes, with its frequency etc
# Frequencies for 12 chromatic notes
note_freqs = {
    'C': 261.63,
    'C#': 277.18, 'Db': 277.18,
    'D': 293.66,
    'D#': 311.13, 'Eb': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99, 'Gb': 369.99,
    'G': 392.00,
    'G#': 415.30, 'Ab': 415.30,
    'A': 440.00,
    'A#': 466.16, 'Bb': 466.16,
    'B': 493.88,
    'R': None  # Rest
}

#TODO hardcode mapping of notes (color -> note)