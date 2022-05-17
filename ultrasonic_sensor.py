import RPi.GPIO as GPIO
import time

#set GPIO Pins
trigger_pin = 8
echo_pin = 10
led_pin = 22

#set GPIO direction (IN / OUT)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.output(trigger_pin, False)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(trigger_pin, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echo_pin) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echo_pin) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if name == 'main':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

            if (dist < 40):
                GPIO.output(GPIO_LED, True)
                print("User Detected")
            else:
                GPIO.output(GPIO_LED, False)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
