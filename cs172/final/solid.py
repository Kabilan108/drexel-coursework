# CS 172 - Final Exam
# Purpose: Define `Solid` abstract base class
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.20.2023

from abc import ABC, abstractmethod


class Solid(ABC):
    """ABC for solid shapes"""

    __ID = -1

    def __init__(self, kind, color="red"):
        """Class constructor"""
        self.__kind = kind
        self.__color = color
        Solid.__ID += 1
        self.__ID = Solid.__ID

    def getKind(self):
        """Getter for kind attribute"""
        return self.__kind

    def getColor(self):
        """Getter for color attribute"""
        return self.__color

    def getID(self):
        """Getter for ID attribute"""
        return self.__ID

    def setColor(self, color):
        """Setter for color attribute"""
        self.__color = color

    @abstractmethod
    def getVolume(self):
        """Abstract method to get volume of solid"""
        pass

    def __str__(self):
        """String representation of solid"""
        return (
            f"Solid ID: {self.__ID}\n"
            f"Solid Kind: {self.__kind}\n"
            f"Solid Color: {self.__color}"
        )
