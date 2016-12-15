#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.output(GPIO_TRIGGER,0)

GPIO.setup(GPIO_ECHO, GPIO.IN)
time.sleep(0.2)

print "Waiting to settle"


# set Trigger to HIGH
GPIO.output(GPIO_TRIGGER, 1)
print("Trigger high")

# set Trigger after 0.01ms to LOW
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, 0)
print("Trigger low")

# save StartTime
while GPIO.input(GPIO_ECHO) == 0:
#	print("Started a start time")
	pass
StartTime = time.time()
print("Saved a start time")
#	time.sleep(0.25)

# save time of arrival
while GPIO.input(GPIO_ECHO) == 1:
	pass
StopTime = time.time()
print("Saved an end time")

# time difference between start and arrival
TimeElapsed = StopTime - StartTime
print("Calculated elapsed time")
# multiply with the sonic speed (34300 cm/s)
# and divide by 2, because there and back
distance = (TimeElapsed * 34300) / 2
print ("Measured Distance = %.1f cm" % distance)
#time.sleep(1)
GPIO.cleanup()
