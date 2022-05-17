# Import Raspberry Pi pin library and time library
import RPi.GPIO as GPIO

# Setup the pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import stepper


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('This is a conveyor test')
    stepper.act(0, 512, "cw")
    print('This is a roller test')
    stepper.act(1, 512, "cw")

