#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:35:58 2020

@author: student
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50), (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                print(1)
                print(event)

pygame.quit()