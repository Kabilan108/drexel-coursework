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

    # Create the screen
    screen = pygame.display.set_mode((800, 600))

    # Set the title and icon
    pygame.display.set_caption("Ball Stack")
    icon = pygame.image.load('ball.png')
    pygame.display.set_icon(icon)

    # Create the game objects
    ball = Ball(400, 300, True, 10, (255, 255, 255))
    block = Block(400, 300, True, 20, 20, (255, 255, 255))
    text = Text(10, 10, True, "Score: 0", (255, 255, 255))

    # Game loop
    running = True
    while running:
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the game objects
        ball.draw(screen)
        block.draw(screen)
        text.draw(screen)

        # Update the display
        pygame.display.update()

        # Check for events
        for event in pygame.event.get():
            # Check for quit event
            if event.type == pygame.QUIT:
                running = False

            # Check for key press event
            if event.type == pygame.KEYDOWN:
                # Check for escape key
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Check for space key
                if event.key == pygame.K_SPACE:
                    # Check if the ball is inside the block
                    if block.get_rect().colliderect(ball.get_rect()):
                        # Increase the score
                        score = int(text.getText().split(": ")[1]) + 1
                        text.setText(f"Score: {score}")

                        # Move the ball to a random location
                        ball.setLoc(
                            random.randint(0, 800),
                            random.randint(0, 600)
                        )

                        # Increase the size of the block
                        # block.setSize(
                        #     block.getWidth() + 10,
                        #     block.getHeight() + 10
                        # )

    # Quit pygame
    pygame.quit()