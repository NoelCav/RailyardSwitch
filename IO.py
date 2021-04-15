#Rasberry Pi Automated Railswitch Control
#
#By: Noel Caverly

import gpiozero
#from RPIO import PWM
import time

#Constants 
STEPPING_PIN = 18 #12 is linked
DIRECTION_PIN = 13 
ACTIVE_PIN = 6 
PEDALFW_PIN = 14
PEDALBW_PIN = 15
WARNING_PIN = 23


#INITIALIZE


#PWM
#switchMotor = gpiozero.PhaseEnableMotor(DIRECTION_PIN, STEPPING_PIN)
pedal = gpiozero.Motor(PEDALFW_PIN, PEDALBW_PIN)
warningLED = gpiozero.LED(WARNING_PIN)

#PINS
motorState = gpiozero.DigitalOutputDevice(ACTIVE_PIN)
motorDirection = gpiozero.DigitalOutputDevice(DIRECTION_PIN) #On is forward, off is backward
motorClk = gpiozero.DigitalOutputDevice(STEPPING_PIN)


#switch

def step(steps):
    if (steps % 1 != 0):
        return
    motorState.on()
    if (steps < 0):
        motorDirection.off()
        steps = -steps
    else:
        motorDirection.on()
    while (steps > 0):
        motorClk.on()
        time.sleep(.3)
        motorClk.off()
        time.sleep(.3)
        steps -= 1
    motorState.off()


# def switchForward(speed=1):
#     motorState.on()
#     switchMotor.forward(speed)


# def switchStop():
#     motorState.off()

# def switchBackward(speed=1):
#     motorState.on()
#     switchMotor.backward(speed)


#pedal

def pedalForward():
    pedal.forward()

def pedalBackward():
    pedal.backward()

def pedalStop():
    pedal.stop()


#Led

def warningFlash():
    warningLED.blink()

def warningStop():
    warningLED.off()






    
            




