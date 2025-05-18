# Default GREEN for creation mode
def turnOnLed(indexLed, color="GREEN"):
    print(f"Turning on led: {indexLed}. Color: {color}")

def turnOffLed(indexLed):
    print(f"Turning off led: {indexLed}")

def play_note(note: str):
    if not note or note == "None":
        print("[Hardware] Skipping empty or 'None' note.")
        return
    try:
        print(f"[Hardware] Playing note: {note}")
        # TODO: Send to speaker
    except Exception as e:
        print(f"[Hardware] ERROR playing note {note}: {e}")


"""Plays the note(s) that should sound at the current column."""
def playColumn(columnIndex: int, boardState: list[tuple[str, str]]):
    if not (0 <= columnIndex < 16):
        print(f"[Hardware] Invalid column index: {columnIndex}")
        return

    try:
        notes_to_play = set()
        note, _ = boardState[columnIndex]

        if note and note != "None":
            notes_to_play.add(note)

        #TODO ANALISAR SE AINDA TEREMOS DUAS+ NOTAS TOCANDO NA MSM COLUNA
        # Check sustained notes in earlier columns  #TODO MAYBE REMOVE IT
        for offset in range(1, 4):
            prev_index = columnIndex - offset
            if prev_index < 0:
                break
            prev_note, prev_duration = boardState[prev_index]
            if not prev_note or prev_note == "None":
                continue
            if (prev_duration == "half" and offset < 2) or (prev_duration == "whole" and offset < 4):
                notes_to_play.add(prev_note)

        print(f"[Hardware] Notes to play at column {columnIndex}: {notes_to_play}")

        for note in notes_to_play:
            play_note(note)
    except Exception as e:
        print(f"[Hardware] ERROR in playColumn: {e}")


#TODO buttons to call respective setter (set_volume, set_tempo, play/stop)
#TODO emergency button resets everything
#TODO communication with esp32
#TODO servo motor
#TODO vibracall