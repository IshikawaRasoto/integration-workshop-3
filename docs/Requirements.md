
# 4.3 Functional Requirements

## 4.3.1 Software Requirements

- **FR01**: The system must detect and classify musical notes placed on the board using the webcam.  
- **FR02**: The system must compare detected notes against the expected melody in guided modes.  
- **FR03**: The system must allow the user to select different sound types for default melody playback.  
- **FR04**: The system must play audio notes corresponding to the notes positioned on the board.  
- **FR05**: The system must continuously play a looping melody based on the placed notes in "Creation" mode.  
- **FR06**: The system must allow the user to control volume and tempo (pacing) through physical buttons.  
- **FR07**: The system must allow the user to control volume and tempo through the web interface.  
- **FR08**: The system must allow the user to select one of the three preloaded songs for guided modes.  
- **FR09**: The system must play a note as a clue in the “Guess the Note” mode.  
- **FR10**: The system must validate note placement in the “Guess the Note” mode and give visual feedback.  
- **FR11**: The system must validate note placement in “Identification” mode using notation concepts:  
  - **FR11.1**: Note name  
  - **FR11.2**: Note duration  
  - **FR11.3**: Measure number  
  - **FR11.4**: Position within the measure  
- **FR12**: The system must provide a default mode that loops through 16 tempos.  
- **FR13**: The system must allow users to configure modes via a web interface.  
- **FR14**: The system must implement the different operational modes as a state machine.  
- **FR15**: The system must support three operational modes:  
  - **FR15.1**: Creation mode (free composition and looped playback)  
  - **FR15.2**: Identification mode (notation-based guided input with 2 preloaded melodies)  
  - **FR15.3**: Guess the Note mode (sound-based input with 3 preloaded melodies)  
- **FR16**: The system must provide visual feedback via RGB LEDs based on interaction.  
- **FR17**: The system must recognize natural (black), flat (blue), and sharp (red) notes based on color detection.  
- **FR18**: The system must allow choosing the sound set for note playback in default mode.  
- **FR19**: The application must follow a multi-layered software architecture.  

---

## 4.3.2 Hardware Requirements

- **FR20**: The system must include a Raspberry Pi 4 B as the processing unit.  
- **FR21**: The system must include a mounted webcam for note detection.  
- **FR22**: The system must include two light sources for consistent image capture.  
- **FR23**: The system must include a speaker to output audio for feedback and playback.  
- **FR24**: The system must have physical buttons for:  
  - **FR24.1**: Volume up  
  - **FR24.2**: Volume down  
  - **FR24.3**: Frequency up  
  - **FR24.4**: Frequency down  
  - **FR24.5**: Play  
  - **FR24.6**: Stop  
- **FR25**: The system must have a stable power supply for all components.  

---

# 4.4 Mechanical Requirements

- **MR01**: The board must be painted or drawn with a blank music sheet layout.  
- **MR02**: The board must contain 4 measures (compasses), each with 4 tempos, totaling 16 positions.  
- **MR03**: Each tempo must have a precise hole for placing musical note pieces.  
- **MR04**: Holes must be arranged in 4 columns per measure, representing note positions and time.  
- **MR05**: Each tempo must include an RGB LED for interactive feedback.  
- **MR06**: The board must have space to accommodate physical musical pieces for melody creation.  
- **MR07**: The board must support pieces representing different note durations:  
  - **MR07.1**: X whole note (semibreve) pieces  
  - **MR07.2**: X half note (minim) pieces  
  - **MR07.3**: X quarter note (crotchet) pieces  
- **MR08**: The board must represent 2 octaves.  
- **MR09**: The board must include a mechanical structure to hold the webcam and light sources overhead.  
- **MR10**: The board must be smaller than 1.2 meters in length to support portability and classroom use.  
- **MR11**: The board must include rhythm control functionality.  

---

# 4.5 Non-Functional Requirements

- **NFR01**: The system must perform all image processing locally on the Raspberry Pi 4 B.  
- **NFR02**: The system must operate reliably under standard indoor lighting conditions.  
- **NFR03**: The web interface and physical interactions must be intuitive and accessible for children aged 6–12.  
- **NFR04**: The system must help introduce basic concepts of musical notation, including:  
  - **NFR04.1**: Recognition of the 12 chromatic scale notes (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)  
  - **NFR04.2**: Understanding of note durations (whole, half, quarter)  
  - **NFR04.3**: Formation and recognition of 3-note chords (triads)  
  - **NFR04.4**: Introduction to clefs and octaves  
  - **NFR04.5**: Recognition and understanding of time signatures  

---

# 4.6 Out-of-Scope Features

- The system will not teach complete music theory, but will act as a support tool.  
- The system will not export sheet music or generate real-time scores.  
- The system will not include internet/cloud-based services.  
- The system will not support multiplayer or simultaneous multi-user interaction.  
