import RPi.GPIO as GPIO
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

    distance_ground = SPEED_OF_SOUND * duration

    distance_ground *= 100

    return distance_ground

def get_distance_for_servo():
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(TRIG, GPIO.LOW)

    while(GPIO.input(ECHO) == GPIO.lOW):
        start_time()
    while(GPIO.input(ECHO) == GPIO.HIGH):
        end_time = time()

    duration = end_time - start_time

    distance_for_servo = SPEED_OF_SOUND * duration

    distance_for_servo *= 100

    return distance_for_servo

def get_height():

    height = (get_distance_for_servo())**2 - (get_distance())**2

    return height

get_height()

    

    
