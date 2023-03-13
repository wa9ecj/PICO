# Program for a Binary Counter 0-15 Version 2
# Lori Pfahler
# Feb 2023
# https://raw.githubusercontent.com/lpfahler/Pico_Projects/main/binary_counter_version2.py
# updates - Ron Kline 2/22/2023

from machine import Pin
from utime import sleep
# variable for setting the speed of counting
delayTime = .5
# setup the four LEDs
onePlaceLED = Pin(15, Pin.OUT)
twoPlaceLED = Pin(14, Pin.OUT)
fourPlaceLED = Pin(13, Pin.OUT)
eightPlaceLED = Pin(12, Pin.OUT)
sixteenPlaceLED = Pin(11, Pin.OUT)

# use try and except to turn LEDs off when exiting the program
try:
    while True:
        for myNum in range(0, 32, 1):
            # turn myNum into binary string with five digits
            myBin = '{0:05b}'.format(myNum) # 2 is being raised to the 5th power
            print(myBin, '=', myNum)
            # light up the LEDS according to the binary representation
            # separate out digits of the binary string and make these integers
            sixteenPlaceLED.value(int(myBin[0]))
            eightPlaceLED.value(int(myBin[1]))
            fourPlaceLED.value(int(myBin[2]))
            twoPlaceLED.value(int(myBin[3]))
            onePlaceLED.value(int(myBin[4]))

            # a sleep to see the counting
            sleep(delayTime)
            
except KeyboardInterrupt:
    # turn off LEDs
    sixteenPlaceLED.off()
    eightPlaceLED.off()
    fourPlaceLED.off()
    twoPlaceLED.off()
    onePlaceLED.off()