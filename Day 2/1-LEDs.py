#imports
from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
#number refers to the pin on the physical board
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


#1=on, 0=off
print("Turn the lights on...")
red.value(1)
amber.value(1)
green.value(1)

#pause for 5 seconds (?) before continuing next commands
time.sleep(5)

print("Lights off!")
red.value(0)
amber.value(0)
green.value(0)