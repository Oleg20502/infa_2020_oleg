import pygame
from pygame.draw import *
from random import randint

pl_name = input('Enter your name:')

pygame.init()

FPS = 20
X, Y = 1000, 550
screen = pygame.display.set_mode((X, Y))

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
COLORS = [RED, BLUE, YELLOW, lightGREEN, GREEN, MAGENTA, CYAN, PINK]
c_num = len(COLORS)
points = 0

#Если 1 - режим игры меняется
effects = 0

square_num = 5
circle_num = 5
triangle_num = 5
pl_time = 1       #время игры 1 минута

def speed(x_max = 30, x_min = 10, y_max = 30, y_min = 10):
    sp = [randint(x_min, x_max)*(-1)**randint(1,2), randint(y_min, y_max)*(-1)**randint(1,2)]
    return sp
 
    
class ball():
    def __init__(self, speed):
        self.scr_sx = X
        self.scr_sy = Y
        self.type = 'ball'
        self.points = 1
        self.dx = int(speed[0])
        self.dy = int(speed[1])        
        r_max = 60
        r_min = 40
        self.r = randint(r_min, r_max)
        self.dr = int(self.r)
        self.x = randint(self.dr, self.scr_sx-self.dr)
        self.y = randint(self.dr, self.scr_sy-self.dr)
        self.color = COLORS[randint(0, c_num-1)]
        
    def draw_obj(self):
        '''рисует шарик '''
        self.move()
        circle(screen, self.color, (self.x, self.y), self.r)
        
    def move(self):              
        self.x += self.dx
        self.y += self.dy        
        if (self.x <= self.dr or self.x >= self.scr_sx-self.dr):
            self.dx *= -1
        if (self.y <= self.dr or self.y >= self.scr_sy-self.dr):
            self.dy *= -1

    def hit(self, pos):
        point = 1
        self.click = 0
        if (pos[0] - self.x)**2+(pos[1] - self.y)**2 <= self.r**2:
            self.click = 1
        return self.click

    def split(self):
        pass
        
class square():
    def __init__(self, speed):
        self.scr_sx = X
        self.scr_sy = Y
        self.type = 'square'
        self.points = 10
        self.dx = int(speed[0])
        self.dy = int(speed[1])
        a_max = 100
        a_min = 50
        self.a = randint(a_min, a_max)
        self.da = int(self.a)
        w_max = 10
        w_min = 5        
        self.width = randint(w_min, w_max) * randint(0, 1)
        self.x = randint(0, self.scr_sx-self.da)
        self.y = randint(0, self.scr_sy-self.da)
        self.color = COLORS[randint(0, c_num-1)]
    
    def draw_obj(self):
        '''рисует квадрат'''
        self.move()
        rect(screen, self.color, (self.x, self.y, self.a, self.a), self.width)
        
    def move(self):              
        self.x += self.dx
        self.y += self.dy        
        if self.x <= 0 or self.x >= self.scr_sx-self.da:
            self.dx *= -1
        if self.y <= 0 or self.y >= self.scr_sy-self.da:
            self.dy *= -1
    
    def hit(self, pos):
        point = 5
        self.click = 0
        if 0 <= pos[0] - self.x <= self.a and 0 <= pos[1] - self.y <= self.a:
            self.click = 1
        return self.click
        
    def split(self, ef):
        if self.click == 1:
            triangle()
        
        pass

class triangle():
    def __init__(self, speed):
        self.scr_sx = X
        self.scr_sy = Y
        self.type = 'triangle'
        self.points = 5
        self.dx = int(speed[0])
        self.dy = int(speed[1])
        a_max = 100
        a_min = 50
        self.a = randint(a_min, a_max)
        self.da_x = int(self.a)
        self.da_y = round(self.a*0.87)
        w_max = 10
        w_min = 5        
        self.width = randint(w_min, w_max) * randint(0, 1)
        self.x = randint(0, self.scr_sx-self.da_x)
        self.y = randint(self.da_y, self.scr_sy)
        self.color = COLORS[randint(0, c_num-1)]
    
    def draw_obj(self):
        '''рисует треугольник'''
        self.move()
        self.coor = [[self.x, self.y], [self.x+round(self.a/2), self.y-self.da_y], [self.x+self.a, self.y]]
        polygon(screen, self.color, self.coor, self.width)
        
    def move(self):              
        self.x += self.dx
        self.y += self.dy        
        if self.x <= 0 or self.x >= self.scr_sx-self.da_x:
            self.dx *= -1
        if self.y <= self.da_x or self.y >= self.scr_sy:
            self.dy *= -1
    pass
    
    def hit(self, pos):
        self.click = 0
        C = self.coor
        a = (C[0][0]-pos[0])*(C[1][1]-C[0][1])-(C[0][1]-pos[1])*(C[1][0]-C[0][0])
        b = (C[1][0]-pos[0])*(C[2][1]-C[1][1])-(C[1][1]-pos[1])*(C[2][0]-C[1][0])
        c = (C[2][0]-pos[0])*(C[0][1]-C[2][1])-(C[2][1]-pos[1])*(C[0][0]-C[2][0])  
        if a >= 0 and b >= 0 and c >= 0 or a <= 0 and b <= 0 and c <= 0:
            self.click = 1
        return self.click 

def count(Obj, points):
    for obj in Obj:
        if obj.hit(event.pos) == 1:
            points += obj.points
    return points

def split(Obj, sq_p = 2, tr_p = 3):
    del_list =[]
    len_obj = len(Obj)
    for i in range(len_obj):
        obj = Obj[i]
        if obj.hit(event.pos) == 1:
            if obj.type == 'square':
                del_list.append(i)
                for j in range(sq_p): 
                    Obj.append(triangle(speed()))
                    Obj[-1].x = obj.x
                    Obj[-1].y = obj.y
            elif obj.type == 'triangle':
                del_list.append(i)
                for j in range(tr_p): 
                    Obj.append(ball(speed()))
                    Obj[-1].x = obj.x
                    Obj[-1].y = obj.y
            else:
                del_list.append(i)
    for d in del_list: 
        Obj.pop(d)
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

Obj = []
for i in range(circle_num):
    Obj.append(ball(speed()))
for i in range(square_num):
    Obj.append(square(speed()))
for i in range(triangle_num):
    Obj.append(triangle(speed()))
t = 0
while not finished:
    t +=1
    clock.tick(FPS)
    tr, sq = [], []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points = count(Obj, points)
            if effects == 1:
                split(Obj)
    for obj in Obj:    
        obj.draw_obj()
    pygame.display.update()
    screen.fill(WHITE)
    if t == int(1100*pl_time):
        finished = True
    
print(str(pl_name)+'! Your score:', points)
pygame.quit()