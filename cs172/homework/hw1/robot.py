# File Name:   robot.py
# Purpose:     A basic class to represent a robot
# Author:      Adelaida Medlock
# Date:        January 5, 2023

import math

class Robot:
    # constructor
    def __init__(self, level = 3.00):
        self.__distanceTraveled = 0
        self.__batteryLevel = level
        
    # getters
    def getDistanceTraveled(self):
        return self.__distanceTraveled
    
    def getBatteryLevel(self):
        return self.__batteryLevel
    
    # setters
    def charge(self, amount):
        self.__batteryLevel += amount
        
    def moveForward(self, distance):
        self.__distanceTraveled = self.__distanceTraveled + distance
        self.__batteryLevel = self.__batteryLevel * (1.0 - distance/(distance + 1.0))
    
    # helper methods
    def getCurrentSpeed(self):
        speed = math.pow(self.__batteryLevel, 2.0) * 2.0
        return speed
    
    def getEstimatedTimeHome(self):
        time = self.__distanceTraveled / self.getCurrentSpeed()
        return time
