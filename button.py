"""
Button Class

"""

# -*- coding: utf-8 -*-

import pygame.font
import setting

class Button():

    def __init__(self, ai_settings, screen, msg):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 400, 70
        self.button_color = setting.DARK_GRAY
        self.text_color = setting.BLACK
        self.font = pygame.font.SysFont('Arial', 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.pre_msg(msg)

    def pre_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)