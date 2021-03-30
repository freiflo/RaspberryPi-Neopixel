from rpi_ws281x import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)  #ignore warnings
GPIO.setmode(GPIO.BOARD) #use physical pin numbering

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #GPIO 15 as input
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #GPIO 14 as input

# LED strip configuration:
LED_COUNT      = 68      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!). GPIO 18, not Pin 18
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 55      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

COUNT = LED_COUNT;

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#Create Neopixel object
strip.begin()
#initialize library (must be called once before other functions)

while True:
    
    
#Increase/Decrease a line of LEDs from left to right
    if GPIO.input(8) == GPIO.HIGH:
        COUNT = COUNT-1
        if COUNT < 0:
            COUNT = 0
        else:
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.show()
            sleep(0.2)
        
    if GPIO.input(10) == GPIO.HIGH:
        COUNT = COUNT +1
        if COUNT > LED_COUNT:
            COUNT = LED_COUNT
        else:
            strip.setPixelColorRGB(COUNT, 255, 0, 0)
            strip.setPixelColorRGB(COUNT-1, 0, 0, 0)
            strip.show()
            sleep(0.2)

##Move single LED
#     #Increment/Move left
#     if GPIO.input(10) == GPIO.HIGH:
#         COUNT = COUNT+1
#         if COUNT == LED_COUNT:                      #LED_COUNT starts at 0! so no +1 needed
#             COUNT = 0
#             strip.setPixelColorRGB(COUNT, 255, 0, 0)
#             strip.setPixelColorRGB(LED_COUNT-1, 0, 0, 0)
#             strip.show()
#             sleep(0.2)
#         else:
#             strip.setPixelColorRGB(COUNT, 255, 0, 0)
#             strip.setPixelColorRGB(COUNT-1, 0, 0, 0)
#             strip.show()
#             sleep(0.2)
#             
#     #Decrement/Move Right 
#     if GPIO.input(8) == GPIO.HIGH:
#         COUNT = COUNT-1
#         if COUNT == -1:
#             COUNT = LED_COUNT-1                     #LED_COUNT starts at 0! so -1 is needed
#             strip.setPixelColorRGB(COUNT, 255, 0, 0)
#             strip.setPixelColorRGB(0, 0, 0, 0)
#             strip.show()
#             sleep(0.2)
#         else:
#             strip.setPixelColorRGB(COUNT, 255, 0, 0)
#             strip.setPixelColorRGB(COUNT+1, 0, 0, 0)
#             strip.show()
#             sleep(0.2)
# 
# #     strip.setPixelColorRGB(0, 255, 0, 0)
# #     strip.setPixelColorRGB(LED_COUNT-1, 255, 0, 0)
# #     strip.show()
    

        
        
        
    
    
    
    
    