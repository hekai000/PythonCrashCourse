# -*-coding: utf-8 -*-

'''

@author: hekai

@license: (C) Copyright 2013-2018

@contact: 675974119@qq.com

@software: garner

@file: alien_invasion.py

@time: 9/18/18 9:30 PM

@desc:

'''
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    pygame.display.set_caption("Alien Invasion")

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()