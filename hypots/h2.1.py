#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:18:24 2020

@author: student
"""
import pygame
from pygame.draw import *

pygame.init()

# И создать окно:
screen = pygame.display.set_mode((300, 200))

pygame.display.update()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            clock.tick(30)