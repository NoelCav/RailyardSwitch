#Rasberry Pi Automated Railswitch Control
#
#By: Noel Caverly

import gpiozero
#from RPIO import PWM
import time
import controller

#Constants 
STEPPING_PIN = 18 #12 is linked
DIRECTION_PIN = 13 
ACTIVE_PIN = 6 
PEDAL_PIN = 14
WARNING_PIN = 23
OVERRIDE_FW = 16
OVERRIDE_BW = 26


#INITIALIZE
#Override
dialFW = gpiozero.DigitalInputDevice(OVERRIDE_FW)
dialBW = gpiozero.DigitalInputDevice(OVERRIDE_BW)

dialFW.when_activated = lambda: controller.openSwitch
dialBW.when_activated = lambda: controller.closeSwitch

#PWM
#switchMotor = gpiozero.PhaseEnableMotor(DIRECTION_PIN, STEPPING_PIN)
#pedal = gpiozero.Motor(PEDALFW_PIN, PEDALBW_PIN)
warningLED = gpiozero.LED(WARNING_PIN)
#pedalClk = gpiozero.PWMLED(PEDAL_PIN) 
#pedalClk.frequency = 50
pedalClk = gpiozero.DigitalOutputDevice(PEDAL_PIN)


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


def pedalStep(steps):
    pulse = .001
    if steps < 0:
        steps = -steps
        pulse = .002
    pause = .02 - pulse
    while steps > 0:
        pedalClk.on()
        time.sleep(pulse)
        pedalClk.off()
        time.sleep(pause)
        steps -= 1


# def switchForward(speed=1):
#     motorState.on()
#     switchMotor.forward(speed)


# def switchStop():
#     motorState.off()

# def switchBackward(speed=1):
#     motorState.on()
#     switchMotor.backward(speed)


#pedal

# def pedalForward():
#     pedalClk.value = .3
#     pedalClk.blink()

# def pedalBackward():
#     pedalClk.value = .7
#     pedalClk.blink()

# def pedalStop():
#     pedalClk.off()


#Led

def warningFlash():
    warningLED.blink()

def warningStop():
    warningLED.off()






    
            




