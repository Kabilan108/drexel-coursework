#!/home/muaddib/.conda/envs/pygame/bin/python

# CS 172 - Homework 4
#
# Description: Main script for "Ball Stack" game
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.11.2023

from Block import Block
from Ball import Ball
from Text import Text
import pygame
import random


if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    surface.fill((255, 255, 255))
    pygame.display.set_caption("Ball Stack - tko35")
    fps = pygame.time.Clock()

    # Create the ball
    ball = Ball(50, 400, True, 10, (255, 0, 0))

    # Create 9 blocks (stacked in a 3x3 cube)
    blocks = [
        Block(400, 380, True, 20, 20, (0, 0, 255)),
        Block(380, 380, True, 20, 20, (0, 0, 255)),
        Block(360, 380, True, 20, 20, (0, 0, 255)),
        Block(400, 360, True, 20, 20, (0, 0, 255)),
        Block(380, 360, True, 20, 20, (0, 0, 255)),
        Block(360, 360, True, 20, 20, (0, 0, 255)),
        Block(400, 340, True, 20, 20, (0, 0, 255)),
        Block(380, 340, True, 20, 20, (0, 0, 255)),
        Block(360, 340, True, 20, 20, (0, 0, 255))
    ]

    # Score counter
    text = Text(10, 10, True, "Score: 0", (0, 0, 0))

    # Physics variables
    dt = 0.1
    g = 6.67
    R = 0.7
    eta = 0.5

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and 
                                             event.key == pygame.K_q):
                pygame.quit()
                exit()

            # Store the mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_1 = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                pos_2 = pygame.mouse.get_pos()

                # Compute distance between the two points (velocity)
                xv = pos_2[0] - pos_1[0]
                yv = -1 * (pos_2[1] - pos_1[1])

                # Launch the ball
                if abs(yv) > 0.0001:
                    # Current pos
                    x, y = ball.getLoc()

                    # Adjust velocity
                    if y > 400:
                        yv = -R * yv
                        xv = eta * xv
                    else:
                        yv -= g * dt

                    # Update the ball
                    new_x = int(x + dt * xv)
                    new_y = int(y - dt * yv)
                    ball.setLoc((new_x, new_y))

        # Draw the ground plane
        pygame.draw.line(surface, (0, 0, 0), (0, 400), (800, 400), 1)

        # Draw the ball
        ball.draw(surface)

        # Draw the blocks
        for block in blocks:
            block.draw(surface)

        # Draw the score
        text.draw(surface)

        # Update the display
        pygame.display.update()

        # Tick the clock
        fps.tick(60)
