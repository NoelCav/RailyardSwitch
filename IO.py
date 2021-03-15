import RPi.GPIO as GPIO
import time

#Constants
FORWARD__PIN = 11
BACKWARD_PIN = 12


GPIO.setmode(GPIO.BOARD)

GPIO.setup(FORWARD__PIN, GPIO.OUT)
GPIO.setup(BACKWARD_PIN, GPIO.OUT)

Forward()

time.sleep(3)

Backward()

time.sleep(3)

Stop()

GPIO.cleanup()


#IO Functions
def setFWPin(state):
    if state:
        GPIO.output(FORWARD__PIN, GPIO.HIGH)
    else:
        GPIO.output(FORWARD__PIN, GPIO.LOW)

def setBWPin(state):
    if state:
        GPIO.output(BACKWARD_PIN, GPIO.HIGH)
    else:
        GPIO.output(BACKWARD_PIN, GPIO.LOW)

def Forward():
    setBWPin(0)
    setFWPin(1)

def Backward():
    setFWPin(0)
    setBWPin(1)

def Stop():
    setFWPin(0)
    setBWPin(0)