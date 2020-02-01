"""
Game Setting Configuration file

"""
# -*- coding: utf-8 -*-

import sys
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (230, 230, 230)

class Settings():
    # save all the configration in the games

    def __init__(self):
        super().__init__()

        #game init setting

        #screen init
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = GRAY