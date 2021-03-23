# RaspberryPi-Neopixel

WORK IN PROGRESS

Neopixel (WS2812b) LED-Strip controlled with Raspberry Pi

The purpose of this (school-)project is to gain experience with the Raspberry Pi and how to use it to control various things.
In this case a WS2812b LED-Strip will be controlled.

This project has a 2-part goal:

Part 1:

-Basic function, getting the Pi to work with the strip

-Interaction, controlling the strip through an input, specifically moving a single LED (planned: increasing/decreasing a scale) across the strip using two buttons

Part 2:

-Syncing the strip to music (not implemented yet)

Requirements:

-Raspberry Pi (Raspberry Pi 4 Model B used)

-WS2812b LED-Strip

-Powersupply (Powerlink Model LPT2 350W ATX PC Powersupply used)

-Logic Level shifter (74ABT125N Level Shifter used)

-Buttons x 2

-Breadboard

-Jumpercable (Male-Male & Male-Female)

Part 1:
Basic function

Prepare the following circuit:

![image](https://user-images.githubusercontent.com/72065170/112108712-dd67bb80-8bb0-11eb-9eb3-253b68de7269.png)

Make sure to use a suitable powersupply, depending on the length of the LED-strip you might need a lot of power.

Depending on the levelshifter used the wiring might change, the datasheet for the 74ABT125N is provided in the directory.

There are other ways of wiring this circuit here: https://www.thegeekpub.com/15990/wiring-ws2812b-addressable-leds-to-the-raspbery-pi/#:~:text=%20Options%20for%20Wiring%20the%20WS2812b%20to%20the,It%20is%20possible%20in%20a%20pinch...%20More

Execute the following commands on your RaspberryPi to install the WS281X library:

sudo apt-get install build-essential python-dev python-pip unzip wget scons swig

wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && sudo scons && sudo pip install rpi_ws281x

To test everything open the strandtest.py in the library and change the variable LED_COUNT to the number of LEDs on your strip.
Execute the altered strandtest.py using the command: sudo python strandtest.py


Interaction

Prepare the following circuit:

![image](https://user-images.githubusercontent.com/72065170/112120388-751fd680-8bbe-11eb-8781-fa61fd438b65.png)


Code:

from rpi_ws281x import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)  #ignore warnings
GPIO.setmode(GPIO.BOARD) #use physical pin numbering

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #GPIO 15 as input
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #GPIO 14 as input

# LED strip configuration:
LED_COUNT      = 68      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 55      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

COUNT = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#Create Neopixel object
strip.begin()
#initialize library (must be called once before other functions)

while True:
    
    #Increment/Move left
    if GPIO.input(10) == GPIO.HIGH:
        COUNT = COUNT+1
        if COUNT == LED_COUNT:                      #LED_COUNT starts at 0! so no +1 needed
            COUNT = 0
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.setPixelColorRGB(LED_COUNT-1, 0, 0, 0)
            strip.show()
            sleep(0.2)
        else:
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.setPixelColorRGB(COUNT-1, 0, 0, 0)
            strip.show()
            sleep(0.2)
            
    #Decrement/Move Right 
    if GPIO.input(8) == GPIO.HIGH:
        COUNT = COUNT-1
        if COUNT == -1:
            COUNT = LED_COUNT-1                     #LED_COUNT starts at 0! so -1 is needed
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.setPixelColorRGB(0, 0, 0, 0)
            strip.show()
            sleep(0.2)
        else:
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.setPixelColorRGB(COUNT+1, 0, 0, 0)
            strip.show()
            sleep(0.2)
