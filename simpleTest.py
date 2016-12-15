#!/usr/bin/python
import libardrone
from time import sleep
drone = libardrone.ARDrone()

drone.takeoff()

#while(KeyboardInterrupt == 0):
if(KeyboardInterrupt):
	drone.land()
