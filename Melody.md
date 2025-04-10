# Melody - MElodic LOgic for DYnamic learning 🎵

## Intro 🎼

Nowadays many music teachers complain about the lack of interest that children are presenting toward learning new instruments and therefore music theory, due to the fact that new generations are presenting difficulties when dealing with frustration.
Instruments such as piano and violin present a difficult learning curve, of which many children show the behaviour of not having the patience to pass through the initial stages of boring exercises and learning to read musical sheets.

With this problem in mind, we propose the development of an embedded system that will serve as an auxiliary tool for music teachers to teach their students about music sheets and music theory. It will catch the children attention by letting them position the notes in a music sheet template and leeting them hear the melody.

## Project description 📋

The project will work arround a wood board that will be painted on top with a music sheet template.

![PartituraBranca](https://github.com/user-attachments/assets/24a49d9d-935f-4660-8890-c2ee6ce10ac3)

The system in it's default mode of operation will be able playing the melody in a loop as represented below:

![NotesLoopSmall](https://github.com/user-attachments/assets/dc551eb7-6f2f-40a3-91d6-d0e69135febc)

The second mode of operation will be a mode that the system will tell by it's interface to the kid which note it wants. The melody will be pre-determined by a pre-loaded song.

The third mode will be simillar to the second one, it will also want the children to place notes determined by a pre-loaded song. However, the interface will be by sound, the system will play the note and the user should place the note in the right place by it's frequency.

![image](https://github.com/user-attachments/assets/13328c2f-e02f-4356-a31a-22013e4a0186)

## Initial specifications ✔️

![image](https://github.com/user-attachments/assets/32730bdb-0779-461f-88f8-021705e767b6)

### Board Specs 📐

- The board will be painted or drawn with a blank music sheet.
  
- The board will have 4 compass
  
- Each compass will have 4 tempos

- The board will have holes to place in a precise way the notes on the music sheet.

- The holes will be placed trough 4 columns in each compass, each hole representing a single note.

- Each hole`s column will represent one tempo in the compass.

- The board will have in each tempo an RGB LED that will serve as part of the user interface.

- The board should have an structure to hold a webcam and light sources over itself.

- The board must have volume control.

- The board must have tempo (rythm) control.

- The board must be smaller than 1 meter in lenght.

![image](https://github.com/user-attachments/assets/6a7008e7-1987-46b1-9ee6-c036d438014e)

### Functionalities Specs 🔎

- The system will have a default mode of operation that will play in loop the 16 tempos.

- The system will have a mode in which it will tell the user a note, and when placed, the system will check it's placement and tell if it's right or wrong. When the song is finished, it will play the melody.

- The system will have a mode in which it will play a note, and wait for the user to place it in the board. It will check if it's in the right place, and give the user the feedback. When the song is finished, it will play the melody.

- The system will have 3 pre-loaded songs which will be played in the guessing modes.

- The system will let the user control it's volume.

- The system will let the user control the pacing.

- The system will let the user choose different sounds to play each note on the default mode.

- The flat note will be colored as blue.

- The sharp note will be colored as red.

- The natural notes will be colored as black.

![image](https://github.com/user-attachments/assets/783abdef-b896-49bc-9d5f-34d7bf900715)

## Meeting with Professor Ellen Carolina Ott - CAART 🎻💬

A meeting was done with professor Ott to present our project and ask for her opinion. She stated that the project was spetacular and she has been trying to find a project with these caracteristcs for years. Even abroad she didn't find anything like ours. She suggested to implement more colors and different notes tempos. Ms. Ott thinks that the project is great, and it would have a really meaningful impact in the way that music teachers interact with their students.

## Components 📷

We presume the system will have the following items:

- Raspbery PI 4 B

- WebCam

- Board

- 2x light sources

- Speaker

- Music Notes (flats, sharps and naturals)

- Power Supply

## BOM 💵 

| Item | Preço |
| --- | --- |
| Câmera USB | R$ 130,00 |
| Raspberry Pi 4 B | R$ 570,00 |
| Impressão 3D (2 rolos de PLA) | R$ 200,00 |
| Compensado para tabuleiro e suporte da câmera | R$ 70,00 - R$ 300,00 |
| Componentes eletrônicos gerais | R$ 0,00 - R$ 75,00 |
| Total | R$ 970,00 - R$ 1.275,00 |
