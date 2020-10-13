import pygame
from pygame.draw import *
from random import randint
import time as t

#if 1 the player's name and result are recorded
pl_rem = 0
Path = '/home-local/student/infa_2020_oleg/Lab6/Game results.txt'
pl_name = 'Player'
if pl_rem == 1:
    pl_name = input('Enter your name: ')
    with open(Path, 'r') as f:
        data = f.readlines()
    g_dict = dict()
    pl, res = '', 0
    for d in data:
        pl = d.split(',')[0]
        res = int(d.split(',')[1])
        g_dict[pl] = res
        
t.sleep(1)      

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
effects = 1

square_num = 5
circle_num = 3
triangle_num = 4
max_score = square_num*10 + circle_num + triangle_num*5

#время игры in seconds
g_time = 60

def speed(x_max = 20, x_min = 10, y_max = 20, y_min = 10):
    sp = [randint(x_min, x_max)*(-1)**randint(1,2), randint(y_min, y_max)*(-1)**randint(1,2)]
    return sp


class ball():
    def __init__(self, speed, x=0, y=0):
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
        if x == 0:
            x = randint(self.dr, self.scr_sx-self.dr)
        if y == 0:
            y = randint(self.dr, self.scr_sy-self.dr)
        self.x = x
        self.y = y
        if self.x <= self.dr or self.x >= self.scr_sx-self.dr:
            if self.x <= self.dr:
                self.x = self.dr
            else:
                self.x = self.scr_sx-self.dr
        if self.y <= self.dr or self.y >= self.scr_sy-self.dr:
            if self.y <= self.dr:
                self.y = self.dr
            else:
                self.y = self.scr_sy-self.dr
        self.color = COLORS[randint(0, c_num-1)]
        
    def draw_object(self):
        '''рисует шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)
        self.move()
        
    def move(self):              
        if self.x <= self.dr or self.x >= self.scr_sx-self.dr:
            self.dx *= -1
        if self.y <= self.dr or self.y >= self.scr_sy-self.dr:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy  

    def hit(self, pos):
        point = 1
        self.click = 0
        if (pos[0] - self.x)**2+(pos[1] - self.y)**2 <= self.r**2:
            self.click = 1
        return self.click


class square():
    def __init__(self, speed, x=0, y=0):
        self.scr_sx = X
        self.scr_sy = Y
        self.type = 'square'
        self.points = 10
        self.dx = int(speed[0])
        self.dy = int(speed[1])
        a_max = 100
        a_min = 60
        self.a = randint(a_min, a_max)
        self.da = int(self.a)
        w_max = 10
        w_min = 5        
        self.width = randint(w_min, w_max) * randint(0, 1)
        if x == 0:
            x = randint(0, self.scr_sx-self.da)
        if y == 0:
            y = randint(0, self.scr_sy-self.da)
        self.x = x
        self.y = y
        if self.x <= 0 or self.x >= self.scr_sx-self.da:
            if self.x <= 0:
                self.x = 0
            else:
                self.x = self.scr_sx-self.da
        if self.y <= 0 or self.y >= self.scr_sy-self.da:
            if self.y <= 0:
                self.y = 0
            else:
                self.y = self.scr_sy-self.da
        self.color = COLORS[randint(0, c_num-1)]
    
    def draw_object(self):
        '''рисует квадрат'''
        rect(screen, self.color, (self.x, self.y, self.a, self.a), self.width)
        self.move()
            
    def move(self):                     
        if self.x <= 0 or self.x >= self.scr_sx-self.da:
            self.dx *= -1
        if self.y <= 0 or self.y >= self.scr_sy-self.da:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy   
    
    def hit(self, pos):
        point = 5
        self.click = 0
        if 0 <= pos[0] - self.x <= self.a and 0 <= pos[1] - self.y <= self.a:
            self.click = 1
        return self.click
        

class triangle():
    def __init__(self, speed, x=0, y=0):
        self.scr_sx = X
        self.scr_sy = Y
        self.type = 'triangle'
        self.points = 5
        self.dx = int(speed[0])
        self.dy = int(speed[1])
        a_max = 100
        a_min = 60
        self.a = randint(a_min, a_max)
        self.da_x = int(self.a)
        self.da_y = round(self.a*0.87)
        w_max = 10
        w_min = 5        
        self.width = randint(w_min, w_max) * randint(0, 1)
        if x == 0:
            x = randint(0, self.scr_sx-self.da_x)
        if y == 0:
            y = randint(self.da_y, self.scr_sy)
        self.x = x
        self.y = y
        if self.x <= 0 or self.x >= self.scr_sx-self.da_x:
            if self.x <= 0:
                self.x = 0
            else:
                self.x = self.scr_sx-self.da_x
        if self.y <= self.da_x or self.y >= self.scr_sy:
            if self.y <= self.da_x:
                self.y = self.da_x
            else:
                self.y = self.scr_sy
        self.color = COLORS[randint(0, c_num-1)]
    
    def draw_object(self):
        '''рисует треугольник'''
        self.coor = [[self.x, self.y], [self.x+round(self.a/2), self.y-self.da_y], [self.x+self.a, self.y]]
        polygon(screen, self.color, self.coor, self.width)
        self.move()
        
    def move(self):              
        if self.x <= 0 or self.x >= self.scr_sx-self.da_x:
            self.dx *= -1
        if self.y <= self.da_x or self.y >= self.scr_sy:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy 
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
    len_obj = len(Obj)
    del_list, new_objects, new_Obj = [], [], []
    for i in range(len_obj):
        obj = Obj[i]
        if obj.hit(event.pos) == 1:
            del_list.append(i)
            if obj.type == 'square':
                for j in range(sq_p): 
                    new_objects.append(triangle(speed(), obj.x, obj.y))
            elif obj.type == 'triangle':
                for j in range(tr_p): 
                    new_objects.append(ball(speed(), obj.x, obj.y))
                    
    for j in range(len_obj):
        if j not in del_list:
            new_Obj.append(Obj[j])
    new_Obj += new_objects
    return new_Obj
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

Objects = []
for i in range(circle_num):
    Objects.append(ball(speed()))
for i in range(square_num):
    Objects.append(square(speed()))
for i in range(triangle_num):
    Objects.append(triangle(speed()))
    
t1 = t.time()

while not finished:
    clock.tick(FPS)
    tr, sq = [], []
    for obj in Objects:
        obj.draw_object()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points = count(Objects, points)
            if effects == 1:
                Objects = split(Objects)
    pygame.display.update()
    screen.fill(WHITE)
    t2 = t.time()
    if g_time <= t2 - t1:
        finished = True
        print('\nTime is over!')
        
print('\n'+str(pl_name)+'! Your score:', points)
print('\nMax score:', max_score)
if pl_rem == 1:
    if points > max(g_dict.values()):
        print("\nCongratulations! You've set a record!")
    g_dict[pl_name] = points
    new_data = []
    for k,i in g_dict.items():
        pair = ','.join([k, str(i)])
        new_data.append(pair)
    new_data_str = '\n'.join(new_data)
    with open(Path, 'w') as f:
        f.write(new_data_str)

pygame.quit()