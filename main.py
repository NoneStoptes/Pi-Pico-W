# This code will be destroyed at next update, this code saved in morsecode.py


from machine import Pin # Importing from the library function Pin
import time

led = Pin(15, Pin.OUT) # Set led to Pin GP15 and set the pin out
dotTime = 0.3 # time of blink dot, 0.3s
dashTime = dotTime * 3 # Time of blink dash is dot * 3, 0.3s * 3 = 0.9s
on = 1 # set on to value 1
off = 0 # set off to value 0

# while ends when the text has only a-z and A-Z, else the question will be ask again
while True:
    text = input("Write a text : ")
    if text.isalpha(): # Function isalpha returns True if all characters in the string are letters (a-z and A-Z), and False otherwise.
        break
    
# Morzeova azbuka, set to every letter his morse
morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

# Led blink function, The LED will blink for as long as you set it
def ledBlink(blinkTime):
    led.value(on)
    print(float(blinkTime))
    print(blinkTime)
    time.sleep(float(blinkTime))
    led.value(off)
    time.sleep(0.3)

# Play letter function, function get letter(char), function return the letter in morse on the led
def playLetter(symbol):
    for dot in symbol:
        if dot == ".":
            ledBlink(dotTime)
        else:
            ledBlink(dashTime)
    time.sleep(0.7)

for letter in text: # Get every letter of text in a loop
    playLetter(morse[letter.upper()])