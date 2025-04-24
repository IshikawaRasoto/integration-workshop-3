# Functional Requirements

## Software Requirements

- FR01: The system must detect and classify musical notes placed on the board using the webcam.  
- FR02: The system must compare detected notes against the expected melody in guided modes.  
- FR03: The system must allow the user to select different sound sets for note playback in Creation  mode. 
- FR04: The system must play audio notes corresponding to the notes positioned on the board.  
- FR05: The system must support three operational modes:  
  - FR5.1: Creation mode (free composition and looped playback)  
  - FR5.2: Identification mode (notation-based guided input with 2 preloaded melodies)  
  - FR5.3: Guess the Note mode (sound-based input with 3 preloaded melodies)  
- FR06: The system must continuously play a looping melody based on the placed notes in "Creation" mode.  
- FR07: The system must allow the user to control volume and tempo (pacing) through physical buttons.  
- FR08: The system must allow the user to control volume and tempo through the web interface.  
- FR09: The system must allow the user to select one of the three preloaded songs for guided modes.  
- FR10: The system must play a note as a clue in the “Guess the Note” mode.  
- FR11: The system must validate note placement in the “Guess the Note” mode and give visual feedback.  
- FR12: The system must validate note placement in “Identification” mode using notation concepts:  
  - FR12.1: Note name  
  - FR12.2: Note duration  
  - FR12.3: Measure number  
  - FR12.4: Position within the measure  
- FR13: The system must provide a default mode that loops through 16 tempos.  
- FR14: The system must allow users to configure modes via a web interface.  
- FR17: The system must provide visual feedback via Bicolor LEDs (Green/Red) based on interaction.  
- FR18: The colors should have the following colors: ~~**TABLE**~~
- FR20: The system must **help** introduce basic concepts of musical notation, including:  
  - FR20.1: Recognition of the 12 chromatic scale notes (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)  
  - FR20.2: Understanding of note durations (whole, half, quarter)  
  - FR20.3: Formation and recognition of 3-note chords (triads)  
  - FR20.4: Introduction to clefs and octaves  
  - FR20.5: Recognition and understanding of time signatures  
- FR21: The system must provide an accessibility mode for blind users, combining audio cues with tactile feedback (vibrations) to support interaction and navigation.  
- FR22: Melody must allow the student to choose the musical clef  
- FR23: Melody must allow the teacher to control the system through a web application  
  - FR23.1: The teacher can choose the mode on the web interface.
  - FR23.2: There should be a page for each mode
  - FR23.3: Every page can control volume, play, pause and tempo.
  - FR23.4: The initial page is a stand-by mode for the teacher choose the operational mode.

---

## Hardware Requirements

- FR24: The system must include a Raspberry Pi 4 B as the processing unit.  
- FR25: The system must include a mounted webcam for note detection.  
- FR26: The system must include two light sources for consistent image capture.  
- FR27: The system must include a speaker to output audio for feedback and playback.  
- FR28: The system must have one physical button for volume up, volume down, frequency up, frequency down, play and stop.
- FR29: The system must have a stable power supply for all components.  **?? QUAL POWER SUPPLY? ESPECIFICAR**
- FR30: Melody must be able to communicate with another device **?? Qual device? Como? Wifi, UART pro esp32?**  
- FR31: The board and the accessibility module must interface through a connector  **Qual conector? O módulo de acessibilidade seria o que? A board seria o que? Raspberry com esp?**
- FR32: The system will be supplied through a single external cable  **Supplied com o que?**

---

## Mechanical Requirements

- FR33: The board must be painted or drawn with a blank music sheet layout.  
- FR34: The board must contain 4 measures (compasses), each with 4 tempos, totaling 16 positions.  
- FR35: Each tempo must have a precise hole for placing musical note pieces.  
- FR36: Holes must be arranged in 4 columns per measure, representing note positions and time.  
- FR37: Each tempo must include an Bicolor LEDs (Green/Red)  for interactive feedback.  
- FR38: The board must have space to accommodate physical musical pieces for melody creation.  
- FR39: The board must support pieces representing different note durations:  
  - FR39.1: X whole note (semibreve) pieces  
  - FR39.2: X half note (minim) pieces  
  - FR39.3: X quarter note (crotchet) pieces  
- FR40: The board must represent 2 octaves.  
- FR41: The board must include a mechanical structure to hold the webcam and light sources overhead.  
- FR42: The board must be smaller than 1.2 meters in length to support portability and classroom use.  
- FR43: The board must include rhythm control functionality.  
- FR44: Melody must allow the student to place musical notes on a blank musical sheet  
- FR45: Melody must have a visual interface with buttons and LEDs on the board for the user.  
- FR46: Melody must have sound interface for the teacher and student  
- FR47: Melody must be carreable  
- FR48: Melody must have an accessibility module for blind people  
  - FR48.1: The accessibility module must be detachable from the main board  
  - FR48.2: The accessibility module must have a touchable interface  
  - FR48.3: The accessibility module should have a vibrating interface  

---

# Non-Functional Requirements

- NFR01: The system must perform all image processing locally on the Raspberry Pi 4 B.  
- NFR02: The system must operate reliably under standard indoor lighting conditions.  
- NFR03: The web interface and physical interactions must be intuitive and accessible for children aged 6–12.  
- NFR04: The application must follow a multi-layered software architecture.  
- NFR05: The Raspberry Pi 4 B must run software developed in Python.  
- NFR06: The ESP32 microcontroller must run firmware developed in C using the FreeRTOS framework.  
- NFR07: The web interface must be implemented using JavaScript.  
- NFR08: The system must implement the different operational modes as a state machine.  
- NFR09: The system must recognize notes based on color detection.  

---

# Out-of-Scope Features

- The system will not teach complete music theory, but will act as a support tool.  
- The system is **not intended** for children to use **alone**
- The system will not export sheet music or generate real-time scores.  
- The system will not include internet/cloud-based services.  
- The system will not support multiplayer or simultaneous multi-user interaction.
- The system will not have a display.
