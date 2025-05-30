# import RPi.GPIO as gpio
from core import session

BUTTON_GPIO_PINS = [2, 3, 4, 17, 27, 22, 10]
SYSTEM_ON = True 

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
    global SYSTEM_ON
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
        return

    if not SYSTEM_ON:
        print("System is OFF. Press Button 7 to turn ON.")
        return

    if button_index == 0: # Play
        session.start_playback()
        print("Playback started via hardware button.")
    elif button_index == 1: # Stop
        session.stop_playback()
        print("Playback stopped via hardware button.")
    elif button_index == 2: # Volume +
        current_volume = session.state.volume
        session.set_volume(min(100, current_volume + 10))
        print(f"Volume increased to {session.state.volume}% via hardware button.")
    elif button_index == 3: # Volume -
        current_volume = session.state.volume
        session.set_volume(max(0, current_volume - 10))
        print(f"Volume decreased to {session.state.volume}% via hardware button.")
    elif button_index == 4: # Tempo +
        current_tempo = session.state.tempo
        session.set_tempo(min(120, current_tempo + 30))
        print(f"Tempo increased to {session.state.tempo} BPM via hardware button.")
    elif button_index == 5: # Tempo -
        current_tempo = session.state.tempo
        session.set_tempo(max(60, current_tempo - 30))
        print(f"Tempo decreased to {session.state.tempo} BPM via hardware button.")
# # Comentado para PC
def setup_buttons():
    pass
#     gpio.setmode(gpio.BCM)
#     gpio.setwarnings(False)

#     for pin in BUTTON_GPIO_PINS:
#         if pin in BUTTON_GPIO_PINS[2:]:
#             gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)
#         else:
#             gpio.setup(pin, gpio.IN)
#         gpio.add_event_detect(pin, gpio.FALLING, callback=button_callback, bouncetime=300)

try:
    setup_buttons()
    print("Hardware buttons initialized.")
except RuntimeError:
    print("Could not setup GPIO. RPi.GPIO error.")
except Exception as e:
    print(f"An error occurred during hardware setup: {e}")

def cleanup_gpio():
    print("Cleaning up GPIO...")
    # gpio.cleanup()

# QUANDO IMPORTAR ISSO N VAI EXECUTAR
if __name__ == '__main__':
    pass
    # # Comentado para PC
    # print("Loop de teste. Aperte Ctrl+C para sair.")
    # try:
    #     while True:
    #         if not SYSTEM_ON and gpio.input(BUTTON_GPIO_PINS[6]) == gpio.LOW: 
    #             pass 
    # except KeyboardInterrupt:
    #     print("Exiting test mode.")
    # finally:
    #     cleanup_gpio()

#TODO communication with esp32