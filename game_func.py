"""
 Pygame base template for building an Alien Warship Game

 Game Main Entry

"""
# -*- coding: utf-8 -*-

import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

# keyboard down function
def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)

# keyboard up function
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    

#mouse click function
def check_play_button(ai_settings, screen, stats, score, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)

        score.prep_score()
        score.prep_high_score()
        score.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

# system event function
def check_event(ai_settings, screen, stats, score, ship, aliens, bullets, play_button):

    #check the game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score, play_button, ship, aliens, bullets, mouse_x, mouse_y)

# update screen
def update_screen(ai_settings, screen, stats, socre, ship, aliens, bullets, play_button):

    #update the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)
    socre.draw_score()

    if not stats.game_active:
        play_button.draw_button()

    #redraw the screen
    pygame.display.flip()

# --- Bullets functions --- 

#update bullets
def update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets):

    #update bullets
    bullets.update()

    #remove disappeared bulelt
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values(): 
            stats.score += ai_settings.alien_points * len(aliens)
            score.prep_score()

        check_high_score(stats, score)

#fire the bullets
def fire_bullets(ai_settings, screen, ship, bullets):
    # file the bullet
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

# --- alien functions ---

#create alien
def create_alien(ai_settings, screen, aliens, alien_number, row_number):

    alien = Alien(ai_settings, screen)
    
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien_height + 2 * alien_height * row_number

    aliens.add(alien)


#get number of aliens in a line
def get_number_aliens_x(ai_settings, alien_width):

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    return number_alien_x 

def get_number_alien_row(ai_settings, ship_height, alien_height):

    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height)
    number_alien_row = int(available_space_y / (2 * alien_height))

    return number_alien_row

#create alien
def create_fleet(ai_settings, screen, ship, aliens):

    alien = Alien(ai_settings, screen)

    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_alien_row = get_number_alien_row(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_alien_row): 
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

#change alien move directions
def change_fleet_direction(ai_settings, aliens):
    
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    
    ai_settings.fleet_direction *= -1


#check whether alien reaches the edge
def check_fleet_edges(ai_settings, aliens):

    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break

#update aliens position
def update_aliens(ai_settings, stats, screen, score, ship, aliens, bullets):

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, score, ship, aliens, bullets)
    
    check_alien_bottom(ai_settings, stats, screen, score, ship, aliens, bullets)

    if len(aliens) == 0:
        create_fleet(ai_settings, screen, ship, aliens)

# --- Game Stats functions ---

#alien hit the ship
def ship_hit(ai_settings, stats, screen, score, ship, aliens, bullets):

    if stats.ship_left > 0:    
        stats.ship_left -= 1
        score.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

#alien reached the buttom of the base
def check_alien_bottom(ai_settings, stats, screen, score, ship, aliens, bullets):

    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, score, ship, aliens, bullets)
            break

#check whether ship remain
def check_ship_remain(stats):

    if stats.ship_left <= 0:
        return False
    else:
        return True

#check high score
def check_high_score(stats, score):

    if stats.score > stats.high_score: 
        stats.high_score = stats.score
        score.prep_high_score()
