# Import Raspberry Pi pin library and time library
import RPi.GPIO as GPIO
import pigpio
import time

# Setup the pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import stepper
import servo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Door Test")
    servo.act(179)