"""
Alien Class

"""
# -*- coding: utf-8 -*-

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    #Alien init
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_setting = ai_setting

        #load alien image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0 :
            return True

    def update(self):
        
        delta = (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x += delta 
