#Rasberry Pi Automated Railswitch Control
#
#By: Noel Caverly

import gpiozero
#from RPIO import PWM
import time

#Constants 
FORWARD_PIN = 18 #12 is linked
BACKWARD_PIN = 19 #13 is linked
PEDALFW_PIN = 14
PEDALBW_PIN = 15
WARNING_PIN = 6


#INITIALIZE


#PWM

switch = gpiozero.Motor(FORWARD_PIN, BACKWARD_PIN)
pedal = gpiozero.Motor(PEDALFW_PIN, PEDALBW_PIN)
warningLED = gpiozero.LED(WARNING_PIN)



#TESTING
switch.forward()
print("going forward")
time.sleep(10)
switch.backward()
print("backwards")
time.sleep(10)
switch.stop()
print("complete")

