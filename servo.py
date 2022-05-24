# Micro Servo 9g Control class
import RPi.GPIO as GPIO
import pigpio
import time

servo_pin = 18

# Initialise the pin as on output and PWM
pwm = pigpio.pi()
pwm.set_mode(servo_pin, pigpio.OUTPUT)

pwm.set_PWM_frequency(servo_pin, 50)

# Activation function, angle variable of 0 to 180 degree
def act(angle):
    # Ensure the given angle is within range
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    
    # Determine the pulse width for the given angle
    pulse_width = ((angle * 100) / 9) + 500
    
    # Set the pulse width
    pwm.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(2)
    
    # Turn off the pwm to save power
    pwm.set_servo_pulsewidth(servo_pin, 0)
    
    return

