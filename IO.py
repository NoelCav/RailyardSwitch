#Rasberry Pi Automated Railswitch Control
#
#By: Noel Caverly

import RPi.GPIO as GPIO
from RPIO import PWM
import time

#Constants        # Pos Pin  -  Neg Pin
FORWARD_PIN = 12  # 12       -  18
BACKWARD_PIN = 13 # 13       -  19
PEDAL_PIN = 5
WARNING_PIN = 6

INIT_FREQ = 50
DUTY_CYCLE = 90

#INITIALIZE

GPIO.setmode(GPIO.BCM)

GPIO.setup(FORWARD_PIN, GPIO.OUT)
GPIO.setup(BACKWARD_PIN, GPIO.OUT)
GPIO.setup(PEDAL_PIN, GPIO.OUT)
GPIO.setup(WARNING_PIN, GPIO.OUT)

#Hardware PWM
PWM0forward = GPIO.PWM(FORWARD_PIN, INIT_FREQ)
PWM1Backwards = GPIO.PWM(FORWARD_PIN, INIT_FREQ)

#Software PWM (RPIO Library)
PWM2pedal = PWM.Servo()




#TESTING
Forward()

time.sleep(3)

Backward()

time.sleep(3)

Stop()

GPIO.cleanup()


#IO Functions
def setPin(state, pin):
    if state:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def setFWPin(state):
    if state:
        PWM0forward.start(DUTY_CYCLE)
    else:
        PWM0forward.stop()

def setBWPin(state):
    if state:
        PWM1Backwards.start(DUTY_CYCLE)
    else:
        PWM1Backwards.stop()

def Forward():
    setBWPin(0)
    setFWPin(1)

def Backward():
    setFWPin(0)
    setBWPin(1)

def Stop():
    setFWPin(0)
    setBWPin(0)