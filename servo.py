import machine
import time

class Servo:
    def __init__(self, pin_number=12):
        self.pin_number = pin_number
        self.pin = machine.Pin(self.pin_number)
        self.pwm = machine.PWM(self.pin, freq=50)

        self.status_led = machine.Pin(23, machine.Pin.OUT)
        self.is_status_on = False
  
    def reset(self):
        print('Reseting servo')

        self.is_status_on = False
        self.status_led.value(self.is_status_on)

        self.position_default()

    def position_default(self):
        print('Servo - default')

        self.pwm.duty(70)

    def position_on(self, to_default=False):
        print('Servo - on')

        self.is_status_on = True
        self.status_led.value(self.is_status_on)

        self.pwm.duty(82) # max 122

        if to_default:
            time.sleep(2)
            self.position_default()

    def position_off(self, to_default=False):
        print('Servo - off')

        self.is_status_on = False
        self.status_led.value(self.is_status_on)

        self.pwm.duty(58) # min 18
        if to_default:
            time.sleep(2)
            self.position_default()