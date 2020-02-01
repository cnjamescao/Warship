"""
 Pygame base template for building an Alien Warship Game

 Game Main Entry

"""
# -*- coding: utf-8 -*-

import sys
import pygame

def check_event():

    #check the game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_setting, screen, ship):

    #update the screen
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    #redraw the screen
    pygame.display.flip()
    