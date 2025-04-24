# Acronyms

| Acronym | Description                         |
|---------|-------------------------------------|
| HLR     | High Level Requirement              |
| MCFR    | Mechanical Functional Requirement   |
| HWFR    | Hardware Functional Requirement     |
| FWFR    | Firmware Functional Requirement     |
| SWFR    | Software Functional Requirement     |
| MCLLR   | Mechanical Low Level Requirement    |
| HWLLR   | Hardware Low Level Requirement      |
| FWLLR   | Firmware Low Level Requirement      |
| SWLLR   | Software Low Level Requirement      |

---

# Functional Requirements

## High Level Requirements (HLR)

| ID        | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| HLR-01    | Melody must allow the student to place musical notes on a blank musical sheet |
| HLR-02    | Melody must allow the student to choose the musical clef                   |
| HLR-03    | Melody must allow the teacher to control the system through a web application |
| HLR-04    | Melody must have a visual interface on the board for the student           |
| HLR-05    | Melody must have sound interface for the teacher and student               |
| HLR-06    | Melody must be carriable                                                   |
| HLR-07    | Melody must have a freeplay mode                                           |
| HLR-08    | Melody must have 2 gamified modes                                          |
| HLR-08.1  | Melody must have "Guess the Note" mode, in which the student hears a note and positions it on the board |
| HLR-08.2  | Melody must have "Identify the Note" mode, in which the teacher tells a note name and the student positions it on the board |
| HLR-09    | Melody must have an accessibility mode for people with disabilities        |
| HLR-10    | Melody must allow the student to control functional parameters             |

---

## Mechanical Functional Requirements (MCFR)

| ID         | Description                                                            | Parent Requirement |
|------------|------------------------------------------------------------------------|--------------------|
| MCFR-01    | Melody must have a board                                               | HLR-01             |
| MCFR-01.1  | The board must contain a blank musical sheet                           |                    |
| MCFR-01.2  | The board must contain guides for positioning the notes and clefs      |                    |
| MCFR-01.3  | The musical sheet must contain 4 compasses                             |                    |
| MCFR-01.4  | The musical sheet must be in tempo 4/4                                 |                    |
| MCFR-02    | Melody must have physical notes to be positioned on the board          | HLR-01             |
| MCFR-02.1  | The musical note must be colored                                       |                    |
| MCFR-02.2  | The musical note must follow its musical notation format               |                    |
| MCFR-03    | Melody must have physical clefs to be positioned on the board          | HLR-02             |
| MCFR-03.1  | The clefs must be colored                                              |                    |
| MCFR-03.2  | The clefs must follow its musical notation format                      |                    |
| MCFR-04    | Each tempo of a compass must have a LED as an interface                | HLR-04             |
| MCFR-05    | Melody must not exceed 1.20 meters in length                           |                    |
| MCFR-06    | Melody must not exceed 1.00 meter in height                            | HLR-06             |
| MCFR-07    | Melody must have an accessibility module for blind people              | HLR-06             |
| MCFR-07.1  | The accessibility module must be detachable from the main board        | HLR-09             |
| MCFR-07.2  | The accessibility module must have a touchable interface               |                    |
| MCFR-07.3  | The accessibility module should have a vibrating interface             |                    |

---

## Hardware Functional Requirements (HWFR)

| ID         | Description                                                                              | Parent Requirement |
|------------|------------------------------------------------------------------------------------------|--------------------|
| HWFR-01    | Melody must have a camera to identify the notes                                          | HLR-01             |
| HWFR-02    | Melody must communicate with another device                                               | HLR-03             |
| HWFR-03    | Underneath each tempo in a compass must be an LED for tempo representation               | HLR-04             |
| HWFR-03.1  | The LEDs must indicate the current tempo in the music                                     | HLR-07             |
| HWFR-03.2  | The LEDs must indicate the current tempo to position a note in the gamified modes         | HLR-08             |
| HWFR-03.3  | The LEDs must indicate a wrong note positioned in the gamified modes                      | HLR-08             |
| HWFR-04    | Melody must have a speaker to play the musical melody                                     | HLR-05             |
| HWFR-05    | The board and the accessibility module must interface through a connector                 | HLR-06             |
| HWFR-06    | The board must contain buttons to interface with the student                              | HLR-10             |


