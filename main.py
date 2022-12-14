from wifi import Wifi
import time_requests
import machine
from servo import Servo
import time

manual_execute_button = machine.Pin(0, machine.Pin.IN)

servo_motor = Servo()
Wifi.connect()

timer = machine.Timer(-1) # virtual timer

def on_manual_execute_button_rising(pin):
    print(f'Manual execute. Current status {servo_motor.is_status_on} will change to {not servo_motor.is_status_on}')

    if servo_motor.is_status_on:
        servo_motor.position_off(to_default=True)
    else:
        servo_motor.position_on(to_default=True)

def execute():
    print('Executing...')

    utc_time = time_requests.get_current_utc_time()
    utc_time_secs = time.mktime(utc_time)
    print(f'Current UTC time {utc_time}({utc_time_secs})')

    light_on_utc_time, light_off_utc_time = time_requests.get_light_on_off_time(utc_time)
    light_on_utc_time_secs, light_off_utc_time_secs = time.mktime(light_on_utc_time), time.mktime(light_off_utc_time)

    print(f'Todays light on and light off UTC time {light_on_utc_time}({light_on_utc_time_secs}) and {light_off_utc_time}({light_off_utc_time_secs})')
    print(f'Lighting status {servo_motor.is_status_on}')

    if light_on_utc_time_secs - utc_time_secs < 0 and light_off_utc_time_secs - utc_time_secs < 0 and servo_motor.is_status_on:
        print('Doing nothing. Lighting is ON, lets keep it!')
    elif light_on_utc_time_secs - utc_time_secs < 0 and light_off_utc_time_secs - utc_time_secs > 0 and servo_motor.is_status_on:
        print('Switching OFF')
        servo_motor.position_off(to_default=True)
    elif light_on_utc_time_secs - utc_time_secs < 0 and light_off_utc_time_secs - utc_time_secs < 0 and not servo_motor.is_status_on:
        print('Switching ON')
        servo_motor.position_on(to_default=True)

execute() # execute from beggining not waiting timer to pass

timer.init(period=20 * 60 * 1000, # every 20 minutes
          mode=machine.Timer.PERIODIC,
          callback=execute)

manual_execute_button.irq(on_manual_execute_button_rising, machine.Pin.IRQ_RISING)