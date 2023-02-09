# CS 172 - Lab 5
#
# Description: Main script for "Winter Wonderland" game
#      Author: Tony Kabilan Okeke <tko35@drexel.edu>
#        Date: 02.09.2023

from Drawable import Rectangle, Snowflake
from pygame import Surface
import pygame
import random


if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Winter Wonderland - tko35')
    fps = pygame.time.Clock()

    # Create a list of drawable objects
    objects = [
        Rectangle(0, 200, 400, 100, (0, 255, 0)),  # Ground plane
        Rectangle(0, 0, 400, 200, (0, 0, 255))     # Sky plane
    ]

    # Flags for toggling animation (Should snowflakes be snowing?)
    snowing = True

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            # Quit the game if the user presses q or closes the window
            if ((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and 
                                                event.__dict__['key'] == pygame.K_q)):
                pygame.quit()
                exit()

            # Toggle animation if the user presses space
            elif (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE):
                snowing = not snowing

        # Loop through and draw all the objects
        for drawable in objects:
            # Draw the snowflake
            drawable.draw(surface)

            # Increment the y coordinate of the snowflake if it is snowing
            if isinstance(drawable, Snowflake) and snowing:
                # Stop the snowflake if it has its max y coordinate
                if drawable.getLoc()[1] < drawable.getMaxY():
                    drawable.setLoc((drawable.getLoc()[0], drawable.getLoc()[1] + 1))

        # Spawn a new snowflake at a random x location (if it is snowing)
        if snowing:
            # Randomly select max y coordinate for the snowflake (somewhere
            # on the ground plane)
            max_y = random.randint(objects[0].getLoc()[1], objects[0].getLoc()[1] + 100)
            snowflake = Snowflake(random.randint(0, 400), max_y)
            objects.append(snowflake)

        # Update the display 
        pygame.display.update()
        fps.tick(60)
