"""
Game Setting Configuration file

"""
# -*- coding: utf-8 -*-

import sys
import pygame

# Define Static Param
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (230, 230, 230)
DARK_GRAY = (150, 150, 150)

SHIP_SPEED_SLOW = 1
SHIP_SPEED_MED = 5
SHIP_SPEED_FAST = 10
SHIP_LIMIT = 3

BULLET_SPEED_SLOW = 1
BULLET_SPEED_MED = 5
BULLET_SPEED_FAST = 10

ALIEN_SPEED_SLOW = 1
ALIEN_SPEED_MED = 3
ALIEN_SPEED_FAST = 5

ALIEN_DROP_SPEED = 30
ALIEN_MOVE_LEFT = -1
ALIEN_MOVE_RIGHT = 1

ALIEN_POINTS = 50

class Settings():
    # save all the configration in the games

    def __init__(self):
        super().__init__()

        #game init setting

        #screen init
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = GRAY
        
        #ship init
        self.ship_speed_factor = SHIP_SPEED_FAST
        self.ship_limit = SHIP_LIMIT

        #bullet init
        self.bullet_speed_factor = BULLET_SPEED_FAST
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = BLACK

        #alien init
        self.alien_speed_factor = ALIEN_SPEED_FAST
        self.fleet_drop_speed = ALIEN_DROP_SPEED
        self.fleet_direction = ALIEN_MOVE_RIGHT
        self.alien_points = ALIEN_POINTS


