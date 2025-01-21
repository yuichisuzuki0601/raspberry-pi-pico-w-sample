from lib.board.unique_id import get_unique_id
from lib.circuit_element.led import LedPico
from lib.circuit_element.tact_switch import TactSwitch
from lib.common_process import process_wifi_setup
import process_stepping_motor
import process_wifi

led_pico = LedPico()
tact_switch_enter_wifi_setup_mode = TactSwitch('enter_wifi_setup_mode', 21)

print('pico init.')
led_pico.on()
print(f'Unique ID: {get_unique_id()}\n')

try:
    if tact_switch_enter_wifi_setup_mode.status() == TactSwitch.ON:
        process_wifi_setup.process(tact_switch_enter_wifi_setup_mode, 2, 7)
    else:
        #process_stepping_motor.process()
        process_wifi.process()
except BaseException as e:
    print(e)
finally:
    print('pico end.')
    led_pico.off()
