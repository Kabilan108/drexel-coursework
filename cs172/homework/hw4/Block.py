#!/home/muaddib/.conda/envs/pygame/bin/python

# CS 172 - Homework 4
#
# Description: "Ball Stack" Game
#              Implementation of the Block class
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.11.2023

from pygame.surface import Surface
from drawable import Drawable
import pygame


class Block(Drawable):
    """Class to draw a square with a black outline in the current location"""

    def __init__(self, x: int = 0, y: int = 0, visible: bool = True,
                 width: int = 10, height: int = 10, color: tuple = (0, 0, 0)):
        super().__init__(x, y, visible)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface: Surface):
        """Draws the block on the screen"""
        # Draw the block
        pygame.draw.rect(
            surface,
            self.__color,
            [self.getLoc()[0], self.getLoc()[1], self.__width, self.__height],
            width=0
        )
        # Draw the outline
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            [self.getLoc()[0], self.getLoc()[1], self.__width, self.__height],
            width=2
        )

    def get_rect(self):
        """Returns the bounding box of the block"""
        return pygame.Rect(
            self.getLoc()[0],
            self.getLoc()[1],
            self.__width,
            self.__height
        )
