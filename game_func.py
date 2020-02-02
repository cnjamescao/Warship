"""
 Pygame base template for building an Alien Warship Game

 Game Main Entry

"""
# -*- coding: utf-8 -*-

import sys
import pygame

from bullet import Bullet
from alien import Alien

# keyboard down function
def check_keydown_event(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_setting, screen, ship, bullets)

# keyboard up function
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    

# system event function
def check_event(ai_setting, screen, ship, bullets):

    #check the game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

# update screen
def update_screen(ai_setting, screen, ship, aliens, bullets):

    #update the screen
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)

    #redraw the screen
    pygame.display.flip()

# --- Bullets functions --- 

#update bullets
def update_bullets(aliens, bullets):

    #update bullets
    bullets.update()

    #remove disappeared bulelt
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

#fire the bullets
def fire_bullets(ai_setting, screen, ship, bullets):
    # file the bullet
    new_bullet = Bullet(ai_setting, screen, ship)
    bullets.add(new_bullet)

# --- alien functions ---

#create alien
def create_alien(ai_setting, screen, aliens, alien_number, row_number):

    alien = Alien(ai_setting, screen)
    
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien_height + 2 * alien_height * row_number

    aliens.add(alien)


#get number of aliens in a line
def get_number_aliens_x(ai_setting, alien_width):

    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    return number_alien_x 

def get_number_alien_row(ai_setting, ship_height, alien_height):

    available_space_y = (ai_setting.screen_height - 3 * alien_height - ship_height)
    number_alien_row = int(available_space_y / (2 * alien_height))

    return number_alien_row

#create alien
def create_fleet(ai_setting, screen, ship, aliens):

    alien = Alien(ai_setting, screen)

    number_alien_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_alien_row = get_number_alien_row(ai_setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_alien_row): 
        for alien_number in range(number_alien_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

#change alien move directions
def change_fleet_direction(ai_setting, aliens):
    
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    
    ai_setting.fleet_direction *= -1


#check whether alien reaches the edge
def check_fleet_edges(ai_setting, aliens):

    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_setting, aliens)
            break

#update aliens position
def update_aliens(ai_setting, aliens):

    check_fleet_edges(ai_setting, aliens)
    aliens.update()
