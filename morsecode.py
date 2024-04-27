from machine import Pin
import time

def morse():
    ledRed = Pin(15, Pin.OUT)
    ledYellow = Pin(16, Pin.OUT)
    dot = 0.3
    bash = dot * 3
    betweens = dot * 3
    on = 1
    off = 0

    def azbukaL():
        ledRed.value(on)
        time.sleep(dot)
        ledRed.value(off)
        time.sleep(dot)
        ledYellow.value(on)
        time.sleep(bash)
        ledYellow.value(off)
        time.sleep(dot)
        for i in range(2):
            ledRed.value(on)
            time.sleep(dot)
            ledRed.value(off)
            time.sleep(dot)
        time.sleep(betweens)
        

    while True:
        time.sleep(betweens)
        for i in range(4):
            ledRed.value(on)    # Set led turn on
            time.sleep(dot) # Sleep 0.3s
            ledRed.value(off)    # Set led turn off
            time.sleep(dot)
        time.sleep(betweens)
        ledRed.value(on)
        time.sleep(dot)
        ledRed.value(off)
        time.sleep(betweens + dot)
        azbukaL()
        azbukaL()
        for i in range(3):
            ledYellow.value(on)
            time.sleep(bash)
            ledYellow.value(off)
            time.sleep(dot)