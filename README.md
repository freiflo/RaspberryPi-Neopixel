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





