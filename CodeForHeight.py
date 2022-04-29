import RPi.GPIO as GPIO
from math import sin, cos, pi as PI
from time import sleep

#constants
DEBUG = False
CALIBRATIONS =5
CALIBRATION_DELAY =1
TRIGGER_TIME = 0.00001
SPEED_OF_SOUND = 343

# RPi to the broadcom pin layout
GPIO.setmode(GPIO.BCM)

# GPIO pins
TRIG =18
ECHO = 27
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# calibrate function
def calibrate():
    distance_avg = 0
    for i in range (CALIBRATIONS):
        distance = get_distance()
        if(DEBUG):
            print ("--Got {}cm".format(distance))

        distance_avg += distance

        sleep(CALIBRATION_DELAY)

    distance_avg /= CALIBRATIONS





def get_distance():

    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    while (GPIO.input(ECHO) == GPIO.LOW):
        start_time = time()
    while (GPIO.input(ECHO) == GPIO.HIGH):
        end_time = time()

    duration = end - start

    distance = SPEED_OF_SOUND * duration

    distance /= 2

    distance *= 100

    return distance

def get_height():

    height = float(cos(get_distance()/servo_distance()))

get_height()

    

    
