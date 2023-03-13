# Program for a Binary Counter 0-256
# Lori Pfahler
# Feb 2023
# https://raw.githubusercontent.com/lpfahler/Pico_Projects/main/binary_counter_version2.py

# updated to use ws2812 led strip
# Ron Kline 2/28/2023

# WS2812 use *** CAUTION ***
# Please note the WS2812 LEDs can draw more current than traditional LEDs
# the 8 LED strip should be OK with the Pico.  For longer strips, an external
# power supply should be used.

# For the WS2812, the colors are displayed as a mix [R,G,B].
# to decrease brightness using the enclosed library, reduce the values of R,G,B.

from machine import Pin
from utime import sleep
from ws2812 import WS2812   # copy to Pico-> /kepler/libs/ws2812.py

# variable for setting the speed of counting
delayTime = .25

# WS2812 Black wire to ground rail
# WS2812 Red wire to +3.3v rail
# WS2812 Yellow wire to GP0 to connect the ws2812 data IN

# Use GPIO 0 pin to use the eight LEDs 
ws = WS2812(machine.Pin(0),8)

# define a function to turn all LEDs off
# numbers in brackets are Red, Green, and Blue values
def ledsOff():
    ws[0] = [0,0,0]
    ws[1] = [0,0,0]
    ws[2] = [0,0,0]
    ws[3] = [0,0,0]
    ws[4] = [0,0,0]
    ws[5] = [0,0,0]
    ws[6] = [0,0,0]
    ws[7] = [0,0,0]
    ws.write()

# use try and except to turn LEDs off when exiting the program using Ctrl-C.
try:
    while True:
        
        for myNum in range(0, 256, 1):
            # turn myNum into binary string with eight digits
            myBin = '{0:08b}'.format(myNum) # 2 is being raised to the 8th power
            print(myBin, '=', myNum)
            # light up the LEDS according to the binary representation
            # separate out digits of the binary string and make these integers

            # When using the ws2812 strip,
            # LEDs are displayed in the order of Least Significant Bit
            # meaning (int(myBin[7])) is associated with [ws0],
            # Most Significant Bit(int(myBin[0]))is associated with ws[7]. 
            # the number 128 is 10000000 in binary.
            #   MSD           LSB
            #    |             |
            #    1 0 0 0 0 0 0 0   
                 
            if (int(myBin[7])) == 1:
                ws[0] = [255,0,0]    # Red           
            else:
                ws[0] = [0,0,0]
                                               
            if (int(myBin[6])) == 1:
                ws[1] = [255,69,0]     #Orange           
            else:
                ws[1] = [0,0,0]                                  

            if (int(myBin[5])) == 1:
                ws[2] = [255,255,0]     #Yellow      
            else:
                ws[2] = [0,0,0]
                                    
            if (int(myBin[4])) == 1:
                ws[3] = [0,255,0]         #Green  
            else:
                ws[3] = [0,0,0]

            if (int(myBin[3])) == 1:
                ws[4] = [0,0,255]           # Blue
            else:                
                ws[4] = [0,0,0]

            if (int(myBin[2])) == 1:
                ws[5] = [75,0,130]           # Indigo
            else:
                ws[5] = [0,0,0]

            if (int(myBin[1])) == 1:
                ws[6] = [127,0,255]           # Violet
            else:
                ws[6] = [0,0,0]

            if (int(myBin[0])) == 1:
                ws[7] = [255,255,255]      # White     
            else:
                ws[7] = [0,0,0]

            ws.write()           
            sleep(delayTime)
     
except KeyboardInterrupt:
    # turn off LEDs
    ledsOff()
    ws.write()
