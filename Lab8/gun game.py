from random import randrange as rnd, choice
import pygame
import math as m
import time

# print (dir(math))

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





class Ball():
    def __init__(self, screen, speed, x=None, y=None):
        self.screen = screen
        self.scr_sx = X
        self.scr_sy = Y
        #self.type = 'ball'
        self.points = 1
        self.spx = int(speed[0])
        self.spy = int(speed[1]) 
        r_max = 60
        r_min = 40
        self.r = randint(r_min, r_max)
        self.dr = int(self.r)
        self.x = x or randint(self.dr, self.scr_sx-self.dr)
        self.y = y or randint(self.dr, self.scr_sy-self.dr)
        self.color = COLORS[randint(0, len(COLORS)-1)]
        
    def draw_object(self):
        '''рисует шарик '''
        circle(screen, self.color, (self.x, self.y), self.r)
        self.move()
        
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
         
    def hit_check(self, pos):
        self.click = 0
        if (pos[0] - self.x)**2+(pos[1] - self.y)**2 <= self.r**2:
            self.click = 1
        return self.click


class gun():
    self.f2_power = 10
    self.f2_on = 0
    self.an = 1
    # self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target(Ball):
    def __init__(self, screen, speed=[0, 0], x=None, y=None):   
        super().__init__(screen, speed, x, y) 
        self.mass = 10
        self.points = 0
        self.live = 1

class Bullet(Ball):
    def __init__(self, screen, ener, x, y, angle):
        self.mass = 10
        self.g = 9.8
        self.k = 2
        self.dt = 0.1
        super().__init__(screen, speed=[0, 0], x, y)
        self.speed_abs = m.sqrt(2 * ener/self.mass)
        self.spx, self.spy = self.speed_abs * m.cos(angle), self.speed_abs * m.sin(angle)
        
    def move(self):
        self.dx = - k * self.spx * m.abs(self.spx)/self.mass * self.dt
        self.dy = - (k * self.spx * m.abs(self.spx)/self.mass + g) * self.dt
        
        self.pos_check()
        

class Gun():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = COLORS[randint(0, len(COLORS)-1)]
        self.max_energy = 100
        
        def draw(self):
            surfase = pygame.Surface(self.size)
            surfase.set_colorkey(CLEAR)
            g_rect = pygame.Rect((0,0),self.size)
            rect(surfase, self.color, g_rect)
            new_surfase = py.transform.rotate(surfase, self.angle)
            Rect = new_surfase.get_rect()  
            Rect.topleft = (self.x, self.y)                
            self.screen.blit(new_surfase, Rect)

        def angle_change(self, event=0):
            if event:
                self.angle = m.atan((event.y-self.x) / (event.x-self.y))
            
        
t1 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()