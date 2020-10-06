import pygame
from pygame.draw import *
import numpy as np
pygame.init()

FPS = 20
X, Y = 1800, 900
screen = pygame.display.set_mode((X, Y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0
max_point = 0
t = 0
def speed(x_max = 30, y_max = 30):
    return [randint(-x_max, x_max+1), randint(-y_max, y_max+1)]

'''def count(pos):
    p = 1
    if (pos[0] - x)**2+(pos[1] - y)**2 <= r**2:
        return p
    else:
        return 0
def click(event):
    print(x, y, r)'''    
    
class balls():
    def __init__(self, screen_sizex, screen_sizey):
        self.scr_sx = screen_sizex
        self.scr_sy = screen_sizey
        
    def ball(self, speed):
        r_max = 100
        self.x = randint(r_max, self.scr_sx-r_max)
        self.y = randint(r_max, self.scr_sy-r_max)
        self.r = randint(30, r_max)
        self.speed = speed
        self.color = COLORS[randint(0, 5)]
        
    def draw_ball(self):
        '''рисует новый шарик '''
        self.move()
        circle(screen, self.color, (self.x, self.y), self.r)
        
    def move(self):
        if not (self.scr_sx - self.r > self.x > self.r and self.scr_sy - self.r > self.y > self.r):
            if not self.scr_sx - self.r > self.x > self.r:
                self.speed[0] = - self.speed[0] 
            else:
                self.speed[1] = - self.speed[1]
        dx = int(self.speed[0])
        dy = int(self.speed[1])
        self.x += dx
        self.y += dy
        
    def hit(self, p):
        if (p[0] - self.x)**2+(p[1] - self.y)**2 <= self.r**2:
            return True
        else:
            return False  

pygame.display.update()
clock = pygame.time.Clock()
finished = False

b = balls(X, Y)
b.ball(speed())

while not finished:
    t += 1
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             points += count(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if b.hit(event.pos) == 1:
                b.ball(speed())
                points += 1
    b.draw_ball()
    max_point += 1
    pygame.display.update()
    screen.fill(BLACK)
    
print(points, max_point)
pygame.quit()