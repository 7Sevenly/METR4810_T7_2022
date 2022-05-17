import RPi.GPIO as GPIO


class led():

    def __init__(self, control_pin):
        self.control_pin = control_pin

        GPIO.setup(control_pin, GPIO.out)
        GPIO.output(control_pin, 0)

    def turn_on(self):
        GPIO.output(self.control_pin, 1)

    def turn_off(self):
        GPIO.output(self.control_pin, 0)
