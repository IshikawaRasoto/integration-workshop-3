> [!NOTE]
> The mitigation strategy is only a preview, after discussion it will be created the risk response plan.

| ID   | Risk Description | Probability (1–5) | Impact (1–5) | Risk Coefficient (P × I) | Mitigation Strategy (Preview) |
|------|------------------|-------------------|--------------|--------------------------|---------------------|
| R01  | PCB manufacturing delay or design mistake | 4 | 4 | 16 | Validate PCB with a breadboard prototype; send design early; use universal board |
| R02  | A team member gives up the project | 3 | 5 | 15 | Deliver 80% of the project; have backup responsibilities and documented work ; have assistants on schedule|
| R03  | Problems with Raspberry Pi performance (lag or overheating) | 3 | 4 | 12 | Use proper cooling and optimize image processing code |
| R04  | Physical structure does not fit or align correctly (holes, webcam stand) | 3 | 4 | 12 | Prototype parts before drilling; validate dimensions before final build |
| R05  | Bluetooth complicates interface development and prolongs the development | 3 | 4 | 12 | Start early development; change to wifi |
| R06  | Raspberry Pi burns out | 2 | 5 | 10 | Lend from colleague |
| R07  | Poor RGB LED feedback or sync issues | 3 | 3 | 9  | Test LED logic and connections early |
| R08  | Electronic design error | 3 | 3 | 9  | Conduct thorough schematic reviews and prototype key circuits |
| R09  | Hardware component burns out (e.g., LEDs, speaker) | 4 | 2 | 8  | Keep spare components and test parts before final assembly |
| R10  | Failure in color recognition due to lighting or quality issues | 2 | 4 | 8  | Calibrate lighting early and use high-contrast colors/materials; use color correction in software |
| R11  | Webcam image quality is insufficient for note detection | 2 | 4 | 8  | Try to solve this problem pra adjusting the software and if that doesn't work buy a new camera |
| R12  | Software development takes longer than expected | 2 | 4 | 8  | Divide the tasks needed between the members of the team to complete them in a quick manner |
| R13  | Bad communication between the hardware components | 2 | 3 | 6  | Have a backup way of communication between the hardware, and if that doesnt work, replace the hardware|
| R14  | Fire at the university | 1 | 5 | 5  | Work outside the premises of the University |
| R15  | Delays in delivery of components | 2 | 2 | 4  | Look for replacements on local shops |
| R16  | Components not available in local stores for fast replacement | 2 | 2 | 4  | Buy a replacement component on the internet and/or order it on a local shop |
| R17  | One or more modes fail to work as expected | 2 | 2 | 4  | Adjust the modes in a simple way to at least have a simple working mode |
| R18  | Incompatibility between software and hardware (e.g., GPIO issues, camera integration) | 1 | 3 | 3  | Study new ways of communication between software and hardware |
| R19  | Overbudget due to price changes in components | 1 | 3 | 3  | Change the components to cheaper replacements that are less powerful but works in the project scope |
| R20  | Team disagreement on feature scope or design | 1 | 2 | 2  | Discuss the changes properly, and have a vote to settle the disagreement |
| R21  | Power supply is unstable or insufficient | 1 | 1 | 1  | Replace with a more powerful power supply or make it work with batteries |
