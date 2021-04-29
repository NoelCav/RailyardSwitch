import IO
import time


TURN_STEPS = 200
switchOpen = False

def free():
    return not IO.motorState.value
        

#Network Override Code
def switchaction(message):
    if (message == "/open"):
        openSwitch()
        print("Switch Open")
    elif (message == "/close"):
        closeSwitch()
        print("Switch Closed")
    else:
        print("Invalid Action")

#Forward is Open, backwards is closed
def closeSwitch():
    print("Closing switch...")
    if not free():
        print("Switch busy.")
        return -1
    if (not switchOpen):
        print("Switch already closed.")
        return -1
    else:
        reverseSwitch()
        return 1


def openSwitch():
    print("Opening switch...")
    if not free():
        print("Switch busy.")
        return -1
    if (switchOpen):
        print("Switch already open.")
        return -1
    else:
        reverseSwitch()
        return 1
        
# Helper Functions

def openPedal():
    global switchOpen
    if switchOpen:
        IO.step(1)
    else:
        IO.step(-1)
    IO.pedalStep(30)



def closePedal():
    IO.pedalStep(-30)


def reverseSwitch():
    if not free():
        print("Switch busy.")
        return -1
    openPedal()
    turn = TURN_STEPS
    global switchOpen
    if (switchOpen):
        turn = turn*-1
    IO.step(turn/2)
    closePedal()
    IO.step(turn/2)
    switchOpen = not switchOpen


        
