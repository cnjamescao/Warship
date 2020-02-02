"""
 Pygame base template for building an Alien Warship Game

 Game Main Entry

"""
# -*- coding: utf-8 -*-

import sys 
import pygame

import game_func as gf
from setting import Settings
from ship import Ship
from pygame.sprite import Group 

class Alien_Warship():

    def __init__(self):
        super().__init__()

    def run_game(self):
        # game init
        pygame.init()
        
        # Set the width and height of the screen [width, height], and set Title of the game
        ai_settings = Settings()

        size = (ai_settings.screen_width, ai_settings.screen_height)
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Alien Invasion")
        
        # Loop until the user clicks the close button.
        done = False
        
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        # prepare for the war ship drawing
        ship = Ship(ai_settings, screen)

        # prepare for bullets
        bullets = Group()

        # prepare for aliens
        aliens = Group()

        gf.create_fleet(ai_settings, screen, ship, aliens)
        
        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            gf.check_event(ai_settings, screen, ship, bullets)
            
            ship.update()
            
            gf.update_bullets(aliens, bullets)

            gf.update_aliens(ai_settings, aliens)

            # --- Game logic should go here
        
            # --- Drawing code should go here
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
            # --- Limit to 60 frames per second
            clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Alien_Warship()
    ai.run_game()