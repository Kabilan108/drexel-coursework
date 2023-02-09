#!/home/muaddib/.conda/envs/pygame/bin/python

#File:      blankPygameV2.py
#Purpose:   Demo of a basic program using pygame
#Author:    A. Medlock
#Date:      February 3, 2021

import pygame

pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Kitty!')

while True: #main game loop
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    catImg = pygame.image.load('cat.png')
    catX = 304
    catY = 204
    surface.blit(catImg, (catX, catY))
    
    fontObj = pygame.font.Font("freesansbold.ttf", 24)
    textSurface = fontObj.render("Kitty Cat!", True, (255, 255, 255))
    surface.blit(textSurface, (10, 10))
    
    
    pygame.display.update()
