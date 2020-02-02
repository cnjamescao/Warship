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
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # game init
    pygame.init()
    
    # Set the width and height of the screen [width, height], and set Title of the game
    ai_settings = Settings()

    size = (ai_settings.screen_width, ai_settings.screen_height)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    lose_button = Button(ai_settings, screen, "You Lose! Start Again")
    
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

    stats = GameStats(ai_settings)

    score = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    center_button = play_button
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        gf.check_event(ai_settings, screen, stats, score, ship, aliens, bullets, center_button)
        
        if stats.game_active:

            if center_button == lose_button:
                center_button = play_button

            ship.update()
            
            gf.update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets)

            gf.update_aliens(ai_settings, stats, screen, score, ship, aliens, bullets)
        
        if not gf.check_ship_remain(stats):
            center_button = lose_button

        # --- Drawing code should go here
        gf.update_screen(ai_settings, screen, stats, score, ship, aliens, bullets, center_button)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

run_game()