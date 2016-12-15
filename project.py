#!/usr/bin/python
import libardrone
from time import sleep

#Sonar imports
import RPi.GPIO as GPIO
import time

#Sonar Setup
GPIO.setmode(GPIO.BCM)
trigFront = 2
echoFront = 3
trigLeft = 14
echoLeft = 15
trigRight = 17
echoRight = 27

frontDist = 0.0
leftDist = 0.0
rightDist = 0.0
timeTravel = 0.0

drone = libardrone.ARDrone()

#Distance Function Definition
def getDistance( trigPin, echoPin ):
	GPIO.setup(trigPin, GPIO.OUT)
	GPIO.setup(echoPin, GPIO.IN)
	GPIO.output(trigPin,0)
	
	# set Trigger to HIGH
	GPIO.output(trigPin, 1)
	time.sleep(0.00001)
	GPIO.output(trigPin, 0)
	
	# save StartTime
	while GPIO.input(echoPin) == 0:
		StartTime = time.time()

	# save time of arrival
	while GPIO.input(echoPin) == 1:	
		StopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2
	#Ensures there is a 2 foot space buffer around drone and accounts
	#for the distance from sonar to edge of drone bumper.
	distance = distance - 92 
	
	return distance

sleep(60)
drone.takeoff()
counter = 0

#Polling Loop
while(counter <= 6):
	
	frontDist = getDistance( trigFront, echoFront )
	print ("Front Distance = %.1f cm" % frontDist)
	leftDist = getDistance( trigLeft, echoLeft )
	print ("Left Distance = %.1f cm" % leftDist)
	rightDist = getDistance( trigRight, echoRight )
	print ("Right Distance = %.1f cm" % rightDist)

	#orientation to the front 
	if ((frontDist > leftDist) and (frontDist > rightDist)):
		timeTravel = frontDist / 500
		drone.move_forward()
                sleep(timeTravel)

        if ((leftDist > frontDist) and (leftDist > rightDist)):
	        timeTravel = leftDist / 500
                drone.move_left()
                sleep(timeTravel)

        if ((rightDist > frontDist) and (rightDist > leftDist)):
                timeTravel = rightDist / 500
                drone.move_right()
                sleep(timeTravel)
	if(counter >= 5):
		drone.land()
		print "Drone land command sent"

       
	drone.hover()
	counter = counter + 1
	print ("Counter = %d" % counter)