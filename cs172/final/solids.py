# CS 172 - Final Exam
# Purpose: Define derived classes `Sphere` and `Cone`
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.20.2023

from solid import Solid
from math import pi


class Sphere(Solid):
    """Derived class for spheres"""

    def __init__(self, radius, color="red"):
        """Class constructor"""
        super().__init__(kind="sphere", color=color)
        self.__radius = radius

    def getRadius(self):
        """Getter for radius attribute"""
        return self.__radius

    def setRadius(self, radius):
        """Setter for radius attribute"""
        self.__radius = radius

    def getVolume(self):
        """Calculate volume of sphere"""
        return (4 / 3) * pi * self.getRadius() ** 3

    def __str__(self):
        """String representation of sphere"""
        s = super().__str__()
        s += f"Volume: {self.getVolume():.2f}\nRadius: {self.getRadius():.2f}"
        return s


class Cone(Solid):
    """Derived class for cones"""

    def __init__(self, radius, height, color="red"):
        """Class constructor"""
        super().__init__(kind="cone", color=color)
        self.__radius = radius
        self.__height = height

    def getRadius(self):
        """Getter for radius attribute"""
        return self.__radius

    def getHeight(self):
        """Getter for height attribute"""
        return self.__height

    def setRadius(self, radius):
        """Setter for radius attribute"""
        self.__radius = radius

    def setHeight(self, height):
        """Setter for height attribute"""
        self.__height = height

    def getVolume(self):
        """Calculate volume of sphere"""
        return (1 / 3) * pi * self.getRadius() ** 2 * self.getHeight()

    def __str__(self):
        """String representation of sphere"""
        s = super().__str__()
        s += (
            f"Volume: {self.getVolume():.2f}\nRadius: {self.getRadius():.2f}"
            f"\nHeight: {self.getHeight():.2f}"
        )
        return s
