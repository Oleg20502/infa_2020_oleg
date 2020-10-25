from random import randint
import pygame as py
from pygame.draw import *
import math as m
import numpy as np
import time

py.init()
FPS = 50
X, Y = 1000, 550
screen = py.display.set_mode((X, Y))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
lightGREEN = (0, 255, 0)
GREEN = (0, 180, 64)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
PINK = (230, 50, 230)
CLEAR = (0, 0, 0, 0)
COLORS = [RED, BLUE, YELLOW, lightGREEN, GREEN, MAGENTA, CYAN, PINK]

tar_num = 3
points = 0
g_time = 2*60

class Ball():
    def __init__(self, screen, speed, x=None, y=None, r=None, color=None, mass=10):
        self.screen = screen
        self.scr_sx = X
        self.scr_sy = Y
        self.points = 1
        self.spx = int(speed[0])
        self.spy = int(speed[1]) 
        r_max = 40
        r_min = 20
        self.r = r or randint(r_min, r_max)
        self.dr = int(self.r+1)
        self.x = x or randint(self.dr, self.scr_sx-self.dr)
        self.y = y or randint(self.dr, self.scr_sy-self.dr)
        self.color = color or COLORS[randint(0, len(COLORS)-1)]
        
    def draw_object(self):
        '''рисует шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)
        
    def pos_check(self):
        if self.x <= self.dr or self.x >= self.scr_sx-self.dr:
            self.spx *= -1
            if self.x <= self.dr:
                self.x = self.dr
            else:
                self.x = self.scr_sx-self.dr
        if self.y <= self.dr or self.y >= self.scr_sy-self.dr:
            self.spy *= -1
            if self.y <= self.dr:
                self.y = self.dr
            else:
                self.y = self.scr_sy-self.dr
        
    def move(self):
        self.x += self.spx
        self.y += self.spy
        self.pos_check()
         
    def hit_check(self, other):
        self.hit = 0
        if (other.x - self.x)**2+(other.y - self.y)**2 <= (other.r + self.r)**2:
            self.hit = 1
        return self.hit 


class Target(Ball):
    def __init__(self, screen, speed=[0, 0], x=None, y=None):   
        super().__init__(screen, speed, x, y)
        self.mass = 10
        self.points = 1
        self.live = 1


class Bullet(Ball):
    def __init__(self, screen, ener, x, y, angle, r):
        self.live = 1
        self.g = 2
        self.mass = 1
        self.k = 0.05
        self.dt = 1
        speed_abs = 7 * m.sqrt(2 * ener/self.mass)
        speed = [speed_abs * m.cos(angle), - speed_abs * m.sin(angle)]
        super().__init__(screen, speed, x, y, r)
        
    def move1(self):
        self.spx += - self.k * self.spx /self.mass * self.dt
        self.spy +=  -(self.k * self.spy /self.mass - self.g) * self.dt
        self.x += round(self.spx * self.dt)
        self.y += round(self.spy * self.dt)
        self.pos_check()
        

class Gun():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 15
        self.color = COLORS[randint(0, len(COLORS)-1)]
        self.max_energy = 100
        self.energy = 10
        
        self.angle = -1
        self.gun_on = 0
        self.shots = 0
        
    def draw_gun(self):
        self.height = max(self.energy, 30)
        Rect0 = np.array([[0, 0], [self.height, 0],
                 [self.height, self.width], [0, self.width]], ndmin=2)
        Trans = np.array([[m.cos(self.angle), m.sin(self.angle)],
                [-m.sin(self.angle), m.cos(self.angle)]], ndmin=2)
        R0 = np.array([[self.x]*4, [self.y]*4], ndmin = 2)
        self.Rect = Rect0 @ Trans.T + R0.T
        polygon(self.screen, self.color, self.Rect)
        
    def fire(self):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.shots += 1
        bul = Bullet(self.screen, self.energy, self.x, self.y, self.angle, 15)
        self.gun_on = 0
        self.energy = 10
        return bul

    def targetting(self, event=1):
        """Прицеливание. Зависит от положения мыши."""
        coord = py.mouse.get_pos()
        w, h = coord[0]-self.x, coord[1]-self.y
        if w != 0:
            self.angle = 1/ 1 * m.atan(-h / w)
        elif h <= 0:
            self.angle = -3.14/2
        else:
            self.angle = 3.14/2
        self.draw_gun()
        
    def fire_start(self):
        self.gun_on = 1

    def power_up(self):
        if self.gun_on == 1 and self.energy < self.max_energy:
            self.energy += 1


targets = []
for i in range(tar_num):
    targets.append(Target(screen))
                
g1 = Gun(screen, 20, 450)
bullets = []

py.display.update()
clock = py.time.Clock()
finished = False
T1 = time.time()
while not finished:
    clock.tick(FPS)
    T2 = time.time()
    g1.targetting()
    g1.power_up()
    for t in targets:
        if t.live == 1:
            t.draw_object()
    for event in py.event.get():
        if event.type == py.QUIT or T2 - T1 >= g_time:
            finished = True
        elif event.type == py.MOUSEBUTTONDOWN:
            g1.fire_start()
        elif event.type == py.MOUSEBUTTONUP:
            bul = g1.fire()
            bullets.append(bul)
    for b in bullets:
        for i in range(len(targets)):
            if b.hit_check(targets[i]) and targets[i].live:
                points += 1
                targets[i].live = 0
        b.draw_object()
        b.move1()
    py.display.update()
    screen.fill(WHITE)

print(points)    
py.quit()
