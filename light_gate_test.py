import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO_100 = 13

GPIO.setup(GPIO_100, GPIO.IN)

if __name__ == '__main__':
    
    while(GPIO.input(GPIO_100) == 0):
        print("BLOCKED")
        
    print("75%")