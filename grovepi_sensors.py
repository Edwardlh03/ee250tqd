import sys
sys.path.append('~Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

#Grove Ultrasonic Ranger connected to digital port 2
ultrasonic_ranger = 2
#Potentiometer connectefd ot analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer, "INPUT")

#clear lcd screen before starting main loop
setText("")

while True:
	try:
		# read distance value from ultrasonic ranger and print distance on LCD

		# read threshold from potentiometer

		# format LCD text according to threshold

	except IOError:
		print("Error")
		
