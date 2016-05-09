import sys
import random
import time
import mraa
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import pyupm_ttp223 as ttp223
import pyupm_i2clcd as lcd
import pyupm_mic as upmMicrophone
import pyupm_buzzer as upmBuzzer
from datetime import datetime as dt

###################### Setup devices ############################
chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA,
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO,
          upmBuzzer.SI]

# New knob on AIO pin 0
knob = grove.GroveRotary(0)

# Create the touch object using D7
touch = grove.GroveButton(7)

# Create the button object using D3
button = grove.GroveButton(3)

# Attach microphone to analog port A3
myMic = upmMicrophone.Microphone(1)
threshContext = upmMicrophone.thresholdContext()
threshContext.averageReading = 100
threshContext.runningAverage = 200
threshContext.averagedOver = 1

# Infinite loop, ends when script is cancelled
# Repeatedly, take a sample every 2 microseconds;
# find the average of 128 samples; and
# print a running graph of dots as averages

# Create the lcd object
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
# myLcd.autoscroll()

# Exit Button
exitButton = grove.GroveButton(6)

########################## global variables ###################
averageThreshold = 0
previousKnobValue = int(knob.abs_value())

buttonId = 0
touchId = 1
knobId = 2
micId = 3
buttonMessage = "press the button"
touchMessage = "press the touch"
knobMessage = "turn the knob"
micMessage = "yell, bitch!"
buttonColor = (25, 145, 177)
touchColor = (161, 135, 46)
knobColor = (56, 173, 72)
micColor = (221, 62, 28)

sensorCheckDelay = 1

###################### game functions #############################
def ChangeLcd(lcd, sensorId, message2):
    lcd.clear()
    lcd.home()
    message1 = ""
    color = (123, 123, 123)
    if sensorId == buttonId:
        message1 = buttonMessage
        color = buttonColor
    elif sensorId == touchId:
        message1 = touchMessage
        color = touchColor
    elif sensorId == knobId:
        message1 = knobMessage
        color = knobColor
    elif sensorId == micId:
        message1 = micMessage
        color = micColor

    lcd.setColor(color[0], color[1], color[2])

    lcd.write(message1)
    lcd.setCursor(1, 0)
    lcd.write(message2)

def WelcomAndSetupMic(lcd, delay, myMic):
    global averageThreshold
    lcd.write("Que pedo morro")
    i = delay
    threshSum = 0
    while i >= 0:
        lcd.setColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.2)
        i -= 1

        buffer = upmMicrophone.uint16Array(128)
        len = myMic.getSampledWindow(2, 128, buffer);
        if len:
            thresh = myMic.findThreshold(threshContext, 30, buffer, len)
            # myMic.printGraph(threshContext)
            if(thresh):
                # print(thresh)
                threshSum += thresh

    # print threshSum
    averageThreshold = threshSum/float(delay)
    averageThreshold *= 2
    print averageThreshold
    # print(averageThreshold)

def Yelled(mic):
    buffer = upmMicrophone.uint16Array(128)
    len = myMic.getSampledWindow(2, 128, buffer);
    if len:
        thresh = myMic.findThreshold(threshContext, 30, buffer, len)
        # myMic.printGraph(threshContext)
        if(thresh):
            print (thresh / averageThreshold)
            return (thresh / averageThreshold) > 1

def PressedButton(button):
    return bool(button.value())

def KnobChanged(knob):
    global previousKnobValue
    newValue = int(knob.abs_value())
    hasMoved = abs(previousKnobValue - newValue) > 250
    previousKnobValue = newValue
    return hasMoved


def CheckSensor(intSensor):
    if intSensor == 0:
        return PressedButton(button)
    elif intSensor == 1:
        return PressedButton(touch)
    elif intSensor == 2:
        return KnobChanged(knob)
    else:
        return Yelled(myMic)

def wrong():
    # Create the buzzer object using GPIO pin 5
    buzz = upmBuzzer.Buzzer(5)
    buzz.playSound(chords[5], 100000)
    time.sleep(0.3)
    buzz.playSound(chords[0], 100000)
    time.sleep(0.3)
    del buzz


def correct():
    # Create the buzzer object using GPIO pin 5
    buzz = upmBuzzer.Buzzer(5)
    buzz.playSound(chords[0], 100000)
    time.sleep(0.3)
    buzz.playSound(chords[2], 100000)
    time.sleep(0.3)
    del buzz

def game():
    while True:
		score = 0
		while True:
		    nextSensor = random.randint(0, 3)
		    ChangeLcd(myLcd, nextSensor, "score: " + str(score))
		    time.sleep(sensorCheckDelay)
		    while not CheckSensor(nextSensor):
			# Exit if pressed the exit button
			if exitButton.value() == 1:
			break
		        # the morrito didn't press the correct sensor
		        if CheckSensor((nextSensor+1) % 4) or CheckSensor((nextSensor+2) % 4) or CheckSensor((nextSensor+3) % 4):
		            print "Error morro"
		            # the morrito pressed a wrong sensor
		            wrong()
		            time.sleep(0.5)

		    # the morrito pressed the correct sensor
		    print "Vas bien"
		    correct()
		    score += 1

if __name__ == '__main__':
    WelcomAndSetupMic(myLcd, 10, myMic)
    game()

    # Delete the upmMicrophone object
    del myMic
    del knob
    del button
    del myLcd
    del touch
