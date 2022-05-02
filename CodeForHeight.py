import RPi.GPIO as GPIO
from time import sleep
from math import *

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





def get_ground_distance():

    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    while (GPIO.input(ECHO) == GPIO.LOW):
        start_time = time()
    while (GPIO.input(ECHO) == GPIO.HIGH):
        end_time = time()

    duration = end_time - start_time

    distance_ground = SPEED_OF_SOUND * duration

    distance_ground *= 100

    return distance_ground

def get_mid_distance():
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    while(GPIO.input(ECHO) == GPIO.lOW):
        start_time= time()
    while(GPIO.input(ECHO) == GPIO.HIGH):
        end_time = time()

    duration = end_time - start_time

    mid_distance = SPEED_OF_SOUND * duration

    mid_distance *= 100

    return mid_distance

def get_height_A():

    height_A = math.sqrt((get_ground_distance())**2 - (get_mid_distance())**2)

    return height_A

def get_top_distance():
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    while(GPIO.input(ECHO) == GPIO.LOW):
        start_time = time()
    while(GPIO.input(ECHO) == GPIO.HIGH):
        end_time = time()

    duration = end_time - start_time

    top_distance = SPEED_OF_SOUND * duration

    top_distance *= 100

    return top_distance

def get_height_B():
    height_B = math.sqrt((get_top_distance())**2 - (get_mid_distance())**2)

    return height_B

def get_final_height():
    final_height = height_A() + height_B()

    return final_height
