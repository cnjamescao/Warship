"""
Game Warship file

"""
# -*- coding: utf-8 -*-

import pygame

# define the war ship class
class Ship():

    #War ship init
    def __init__(self, ai_setting, screen):
        super().__init__()

        #init the ship position
        self.screen = screen
        
        #init the ship configration
        self.ai_setting = ai_setting
        
        self.moving_left = False
        self.moving_right = False

        #loading image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put the ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

    def blitme(self):

        #draw the ship at the position
        self.screen.blit(self.image, self.rect)

    def update(self):

        #update the ship position
        if self.moving_left and self.rect.left > 0 :
            self.rect.centerx -= self.ai_setting.ship_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.rect.centerx += self.ai_setting.ship_speed_factor

