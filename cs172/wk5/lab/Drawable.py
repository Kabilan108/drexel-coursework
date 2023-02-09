# CS 172 - Lab 5
#
# Description: Class definition for Drawable objects
#      Author: Tony Kabilan Okeke <tko35@drexel.edu>
#        Date: 02.09.2023

import pygame
from abc import ABC, abstractmethod
from pygame.surface import Surface

class Drawable(ABC):
    def __init__(self, x: int=0, y: int=0):
        self.__x = x
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self, p: tuple):
        self.__x = p[0]
        self.__y = p[1]
    
    @abstractmethod
    def draw(self, surface: Surface):
        pass


class Rectangle(Drawable):
    """Class to create rectangle objects in the game"""
    
    def __init__(self, x: int=0, y: int=0, width: int=0, height: int=0, color: tuple=(0,0,0)):
        """Class constructor"""
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface: Surface):
        """Draws the rectangle on the screen"""
        pygame.draw.rect(
            surface, 
            self.__color, 
            [self.getLoc()[0], self.getLoc()[1], self.__width, self.__height]
        )


class Snowflake(Drawable):
    """Class to create snowflake objects in the game"""

    def __init__(self, x: int=0, max_y: int=300):
        """Class constructor"""
        super().__init__(x, 0)
        self.__max_y = max_y
        self.__color = (255, 255, 255)
        self.__length = 5

    def getMaxY(self):
        """Returns the maximum y coordinate of the snowflake"""
        return self.__max_y

    def draw(self, surface: Surface):
        """
        Draws the snowflake on the screen
        """

        # Define left and right points for each line
        left = [
            (self.getLoc()[0] - self.__length, self.getLoc()[1]),
            (self.getLoc()[0], self.getLoc()[1] - self.__length),
            (self.getLoc()[0] - self.__length, self.getLoc()[1] - self.__length),
            (self.getLoc()[0] - self.__length, self.getLoc()[1] + self.__length)
        ]
        right = [
            (self.getLoc()[0] + self.__length, self.getLoc()[1]),
            (self.getLoc()[0], self.getLoc()[1] + self.__length),
            (self.getLoc()[0] + self.__length, self.getLoc()[1] + self.__length),
            (self.getLoc()[0] + self.__length, self.getLoc()[1] - self.__length)
        ]

        # Draw the lines
        for p1, p2 in zip(left, right):
            pygame.draw.line(surface, self.__color, p1, p2)
