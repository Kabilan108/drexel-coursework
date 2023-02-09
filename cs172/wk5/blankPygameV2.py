#File:      blankPygameV2.py
#Purpose:   Demo of a basic program using pygame
#Author:    A. Medlock
#Date:      February 3, 2021

import pygame

pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

while True: #main game loop
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    pygame.display.update()
