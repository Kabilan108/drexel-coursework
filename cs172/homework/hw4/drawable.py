#!/home/muaddib/.conda/envs/pygame/bin/python

# CS 172 - Homework 4
#
# Description: "Ball Stack" Game
#              Implementation of the Drawable class
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.11.2023

from abc import ABC, abstractmethod
from pygame.surface import Surface


class Drawable(ABC):
    """Abstract Base Class for drawable objects"""

    def __init__(self, x: int=0, y: int=0, visible: bool=True):
        """Class constructor"""
        self.__x = x
        self.__y = y
        self.__visible = visible

    def getLoc(self):
        """Returns the object's location"""
        return (self.__x, self.__y)
    
    def setLoc(self, p: tuple):
        """Sets the object's location"""
        self.__x = p[0]
        self.__y = p[1]

    def isVisible(self):
        """Returns the object's visibility"""
        return self.__visible
    
    def toggleVisibility(self):
        """Toggles the object's visibility"""
        self.__visible = not self.__visible

    @abstractmethod
    def draw(self, surface: Surface):
        """Abstract method for drawing the object"""
        pass

    @abstractmethod
    def get_rect(self):
        """Abstract method for getting the object's bounding box"""
        pass
