#!/home/muaddib/.conda/envs/pygame/bin/python

# CS 172 - Homework 4
#
# Description: "Ball Stack" Game
#              Implementation of the Text class
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.11.2023

from pygame.surface import Surface
from drawable import Drawable
import pygame


class Text(Drawable):
    """Class to display text (score) on the screen"""
    
    def __init__(self, x: int = 0, y: int = 0, visible: bool = True,
                text: str = "", color: tuple = (0, 0, 0)):
        super().__init__(x, y, visible)
        self.__text = text
        self.__color = color

    def draw(self, surface: Surface):
        """Draws the text on the screen"""
        
        # Draw the text
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render(self.__text, True, self.__color)
        surface.blit(text, self.getLoc())

    def get_rect(self):
        """Returns the bounding box of the text"""
        return pygame.Rect(
            self.getLoc()[0],
            self.getLoc()[1],
            0,
            0
        )
