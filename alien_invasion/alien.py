# -*-coding: utf-8 -*-

'''

@author: hekai

@license: (C) Copyright 2013-2018

@contact: 675974119@qq.com

@software: garner

@file: alien.py.py

@time: 9/19/18 10:13 PM

@desc:

'''
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x =  float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)