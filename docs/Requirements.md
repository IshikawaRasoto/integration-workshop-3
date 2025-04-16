# Functional Requirements

- The system must have a "Creation" mode for free music creation
- The "Creation" mode must continuously play the melody created by the student
- The system must have an "Identification" mode for note identification, instructing the student to position the pieces on the board using musical notation concepts (note, duration, measure and position in the measure)
- The “Identification” mode must have two pre-configured melodies
- The system must have a WEB user interface
- The WEB interface must allow mode configuration
- The system must have pieces for melody creation
  - The system must have X whole note pieces
  - The system must have X half note pieces
  - The system must have X quarter note pieces
- The system must have a board with 2 octaves and 4 measures each
- The board must be painted or drawn with a blank music sheet.
- The board must have 4 compass
- Each compass must have 4 tempos
- The board must have holes to place in a precise way the notes on the music sheet.
- The holes must be placed trough 4 columns in each compass, each hole representing a single note.
  - Each hole's column must represent one tempo in the compass.
- The board must have in each tempo an RGB LED that will serve as part of the user interface.
- The board should have an structure to hold a webcam and light sources over itself.
- The board must have rhythm control.
- The board must be smaller than 1 meter in length.
- The system must have a default mode of operation that will play in loop the 16 tempos.
- The system must have a mode in which it will tell the user a note, and when placed, the system will check it's placement and tell if it's right or wrong. When the song is finished, it will play the melody.
- The system must have a mode in which it will play a note, and wait for the user to place it in the board. It will check if it's in the right place, and give the user the feedback. When the song is finished, it will play the melody.
- The system must have 3 pre-loaded songs which will be played in the guessing modes.
- The system must let the user control it's volume.
- The system must let the user control the pacing.
- The system must let the user choose different sounds to play each note on the default mode.
- The flat note must be colored as blue.
- The sharp note must be colored as red.
- The natural notes must be colored as black.
- The board must be have a PCB
- The electronic board must have six buttons
  - Two buttons to control the volume (up/down)
  - Two buttons to change the frequency (up/down)
  - One button to stop
  - One button to play
- The app must have a software with multiples layers
- The system must have three modes
  - mode guess the note
  - mode play the music
  - mode play your own song
- The modes must be a state machine

# Non-Functional Requirements
- RNF01.: The system should help teach basic concepts of musical notation
  - RNF01.1: The system should help teach the 12 musical notes (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)
  - RNF01.2: The system should help teach the durations of semibreve, minim and crotchet notes
  - RNF01.3: The system should help teach 3-note chords (triads)
  - RNF01.4: The system should help teach clefs and octaves
  - RNF01.5: The system should help teach time signatures

# Anti-Requirements
- `!` DEFINIR O QUE NÃO VAI TER