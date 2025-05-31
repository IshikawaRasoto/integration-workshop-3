import RPi.GPIO as gpio
import asyncio
from core import session
from api import manager

BUTTON_GPIO_PINS = [2, 3, 4, 17, 27, 22, 10]
SYSTEM_ON = True 

main_event_loop = None
api_manager = None

def set_main_loop_and_manager(loop, manager_instance):
    """
    Called by main.py to provide the asyncio loop and API manager.
    """
    global main_event_loop, api_manager
    main_event_loop = loop
    api_manager = manager_instance
    print("[Hardware] Main event loop and API manager have been set.")

def turnOnLed(indexLed, color="GREEN"):
    print(f"Turning on led: {indexLed}. Color: {color}")

def turnOffLed(indexLed):
    print(f"Turning off led: {indexLed}")

def emergency_off_actions():
    #TODO RESETAR A RASPBERRY
    #TODO ligou a tomada, executa essa função
    global SYSTEM_ON
    SYSTEM_ON = False
    print("System OFF ")
    for i in range(16): # Assuming 16 LEDs
        turnOffLed(i)

def system_on_actions():
    global SYSTEM_ON
    SYSTEM_ON = True
    #Set to default
    reset_melody()
    print("System ON")

def reset_melody():
    session.set_page("home") 
    session.set_volume(50) 
    session.set_tempo(60)  
    session.set_accessibility(False)
    session.set_note(None)
    session.set_note_index(0)
    session.select_melody(None)

def button_callback(pin):
    global SYSTEM_ON, main_event_loop, api_manager
    try:
        button_index = BUTTON_GPIO_PINS.index(pin)
    except ValueError:
        print(f"Unknown pin {pin} pressed.")
        return

    if button_index == 6: # Turn On/Off button
        if SYSTEM_ON:
            emergency_off_actions()
        else:
            system_on_actions()

        if api_manager and main_event_loop and main_event_loop.is_running():
            asyncio.run_coroutine_threadsafe(api_manager.broadcast_state(), main_event_loop)
            print("[Hardware] System ON/OFF state broadcast scheduled.")
        
        return

    if not SYSTEM_ON:
        print("System is OFF. Press Button 7 to turn ON.")
        return

    action_taken = False
    if button_index == 0: # Play
        session.start_playback()
        print("Playback started via hardware button.")
        action_taken = True
    elif button_index == 1: # Stop
        session.stop_playback()
        print("Playback stopped via hardware button.")
        action_taken = True
    elif button_index == 2: # Volume +
        current_volume = session.state.volume
        session.set_volume(min(100, current_volume + 10))
        print(f"Volume increased to {session.state.volume}% via hardware button.")
        action_taken = True
    elif button_index == 3: # Volume -
        current_volume = session.state.volume
        session.set_volume(max(0, current_volume - 10))
        print(f"Volume decreased to {session.state.volume}% via hardware button.")
        action_taken = True
    elif button_index == 4: # Tempo +
        current_tempo = session.state.tempo
        session.set_tempo(min(120, current_tempo + 30))
        print(f"Tempo increased to {session.state.tempo} BPM via hardware button.")
        action_taken = True
    elif button_index == 5: # Tempo -
        current_tempo = session.state.tempo
        session.set_tempo(max(60, current_tempo - 30))
        print(f"Tempo decreased to {session.state.tempo} BPM via hardware button.")
        action_taken = True

    if action_taken:
        if api_manager and main_event_loop and main_event_loop.is_running():
            future = asyncio.run_coroutine_threadsafe(api_manager.broadcast_state(), main_event_loop)
            try:
                future.result(timeout=1) # Wait for 1 second
                print("[Hardware] Broadcast state successfully scheduled and completed from button callback.")
            except asyncio.TimeoutError:
                print("[Hardware] Warning: Broadcast state scheduling timed out.")
            except Exception as e:
                print(f"[Hardware] Error during broadcast_state: {e}")
        elif not (api_manager and main_event_loop):
            print("[Hardware] Error: API manager or event loop not set. Cannot broadcast.")
        elif not main_event_loop.is_running():
            print("[Hardware] Error: Event loop not running. Cannot broadcast.")


# # Comentado para PC
def setup_buttons():
    # pass
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    for pin in BUTTON_GPIO_PINS:
        if pin in BUTTON_GPIO_PINS[2:]:
            gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        else:
            gpio.setup(pin, gpio.IN)
        gpio.add_event_detect(pin, gpio.FALLING, callback=button_callback, bouncetime=300)

try:
    setup_buttons()
    print("Hardware buttons initialized.")
except RuntimeError:
    print("Could not setup GPIO. RPi.GPIO error.")
except Exception as e:
    print(f"An error occurred during hardware setup: {e}")

def cleanup_gpio():
    print("Cleaning up GPIO...")
    gpio.cleanup()

# QUANDO IMPORTAR ISSO N VAI EXECUTAR
if __name__ == '__main__':
    # pass
    # # Comentado para PC
    print("Loop de teste. Aperte Ctrl+C para sair.")
    try:
        while True:
            if not SYSTEM_ON and gpio.input(BUTTON_GPIO_PINS[6]) == gpio.LOW: 
                pass 
    except KeyboardInterrupt:
        print("Exiting test mode.")
    finally:
        cleanup_gpio()

#TODO communication with esp32