"""
 Game bullet class

"""
# -*- coding: utf-8 -*-

import pygame

from pygame.sprite import Sprite

# class for bullet
class Bullet(Sprite):

    #bullet init
    def __init__(self, ai_setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #set bullet position
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        # update bullet position
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect) 
