"""Proyecto de Cham."""

import pyupm_grove as grove
import pyupm_ttp223 as ttp223
import pyupm_i2clcd as lcd

# Create the touch object using GPIO pin 4
touch1 = ttp223.TTP223(4)
# Create the button object using GPIO pin 8
button = grove.GroveButton(8)
# Create the lcd object
myLcd = lcd.Jhd1313m1(4, 0x3E, 0x62)

def changeLCD(value, cap):
	percentage = float(value) / capacity
	if (percentage <= 0.25):
		myLcd.setColor(255,0,0)
	elif(percentage <= 0.50):
		myLcd.setColor(255,165,0)
	elif(percentage <= 0.75):
		myLcd.setColor(255,255,0)
	elif(percentage <= 1):
		myLcd.setColor(0,255,0)
	myLcd.setCursor(1, 0)
	if(value < 10):
		myLcd.write("Available: " + "0" + str(currentCapacity))
	else:
		myLcd.write("Available: " + str(currentCapacity))
