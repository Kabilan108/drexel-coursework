#!/home/muaddib/.conda/envs/pygame/bin/python

# CS 172 - Homework 4
#
# Description: "Ball Stack" Game
#              Implementation of the Ball class
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.11.2023

from pygame.surface import Surface
from drawable import Drawable
import pygame


class Ball(Drawable):
    """Class to draw a circle in the current location"""

    def __init__(self, x: int = 0, y: int = 0, visible: bool = True,
                 radius: int = 10, color: tuple = (0, 0, 0)):
        super().__init__(x, y, visible)
        self.__radius = radius
        self.__color = color

    def draw(self, surface: Surface):
        """Draws the ball on the screen"""
        pygame.draw.circle(
            surface,
            self.__color,
            self.getLoc(),
            self.__radius
        )

    def get_rect(self):
        """Returns the bounding box of the ball"""
        return pygame.Rect(
            self.getLoc()[0] - self.__radius,
            self.getLoc()[1] - self.__radius,
            self.__radius * 2,
            self.__radius * 2
        )
