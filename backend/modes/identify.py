import asyncio
from core import session, utils
from core import hardware

async def run_mode():
    feedback_led_index = 0  # Using LED 0 for general feedback
    previous_led_color = None # To track current LED state

    # Melody data mapping
    melodies = {
        "Ovelha Preta": utils.OVELHA_PRETA,
        "Ode Alegria": utils.ODE_ALEGRIA,
        "Canon in D": utils.CANON_IN_D
    }

    print("[IdentifyMode] Entered Identify Note Mode")
    try:
        while session.state.page == "identify":
            while(session.state.playing and session.state.melody is not None):
                print("loop")
                current_melody_data = melodies[session.state.melody]
                note_idx = session.state.note_index

                if note_idx >= 16:
                    if previous_led_color:
                        hardware.turnOffLed(feedback_led_index)
                        previous_led_color = None
                    await asyncio.sleep(1)
                    #TODO tocar a melodia a um bpm fixo
                
                expected_note, expected_duration = current_melody_data[note_idx]
                session.set_current_note_and_duration_for_display(expected_note, expected_duration)
                target_duration_display = session.get_duration_display_name(expected_duration)

                if session.state.note != expected_note or session.state.note_duration_display != target_duration_display:
                    session.set_current_note_and_duration_for_display(expected_note, expected_duration)

                # TODO: Read current note from melody using note_index
                # TODO: Use noteDetection to read placed note
                # TODO: Compare detected note to expected note

                # TODO: Green LED if correct, advance index
                # TODO: Red LED if incorrect
                # TODO: Yellow LED if nothing detected
                await asyncio.sleep(0.5) # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)
            await asyncio.sleep(1) # NECESSARY TO DO THE OTHER TASKS (ModeManager etc)


    except asyncio.CancelledError: # when ModeManager does .cancel()
        print("[IdentifyMode] Exited Identify Note Mode")
        raise
        

