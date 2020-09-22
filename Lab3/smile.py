#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:34:56 2020

@author: student
"""
import pygame
from pygame.draw import *
pygame.init()


FPS = 30
screen = pygame.display.set_mode((800, 800))

circle(screen, (255, 255, 0), (100+300, 100+300), 150)
rect(screen, (0, 0, 0), (330, 170+300, 150, 20))
circle(screen, (255, 0, 0), (330, 350), 30)
circle(screen, (0, 0, 0), (330, 350), 13)
circle(screen, (255, 0, 0), (465, 350), 25)
circle(screen, (0, 0, 0), (465, 350), 12)
line(screen, (0, 0, 0), [320, 300], [380, 330], 15)
line(screen, (0, 0, 0), [420, 330], [480, 300], 15)
#rect(screen, (120, 100, 255), (100, 100, 200, 200), 15)
#polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (200, 200), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),(300,100), (100,100)], 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()