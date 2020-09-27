import pygame as py
from pygame.draw import *
screen_X = 1000  
screen_Y = 550  
FPS = 30  

cat_zoom = 1
cat_pos = (600, 350)

window_pos = (700, 50)
window_size = 1.5

clew_pos = (300, 400)
clew_size = 1

wall_height = 350

WHITE = (255, 255, 255)
RED = (225, 0, 50)
BLACK = (0 , 0 , 0) 
lightBLACK = (3,3,3)
lightGreen = (0, 255, 0)
BLUE  = (0,0,255, 20)
GRAY = (125, 125, 125)
lightBlue = (64, 128, 255)
GREEN = (0, 200, 64, 20)
YELLOW = (225, 225, 0, 2)
PINK = (230, 50, 230, 0)
brown = (105, 82, 62, 255)
darkorange3 = (205, 102, 0, 255)
rosybrown5 = (159, 125, 125, 255)
sandybrown = (244, 164, 96, 255)
CLEAR = (0,0,0,0)                     # Прозрачный
pi = 3.14

py.init()
screen = py.display.set_mode((screen_X , screen_Y))   
clock = py.time.Clock()  
screen.fill(WHITE) 

def RotatedEllipse(screen, pos, size, e_color, angle = 0, e_width = 0):
    surfase = py.Surface(size)
    surfase.set_colorkey(CLEAR)
    e_rect = py.Rect((0,0),size)
    ellipse(surfase, e_color, e_rect, e_width)
    ellipse(surfase, lightBLACK, e_rect, 1)
    new_surfase = py.transform.rotate(surfase, angle)
    Rect = new_surfase.get_rect()  
    Rect.center = pos                 
    screen.blit(new_surfase, Rect)

def RotatedTriangle(screen, pos, size, color, angle, width = 5):
    surfase = py.Surface(size)
    surfase.set_colorkey(CLEAR)
    rect = py.Rect((0,0), size)
    polygon(surfase, color, [[0,0], [size[0],0], [int(size[0]/2), size[1]]])
    polygon(surfase, lightBLACK, [[0,0], [size[0],0], [int(size[0]/2), size[1]]], width)
    new_surfase = py.transform.rotate(surfase , angle)
    Rect = new_surfase.get_rect()  
    Rect.topleft = pos
    screen.blit(new_surfase , Rect)  
    
def arc_image(size, color, s_angle, e_angle, width=5, alpha = 255):
    image_surfase = py.Surface((size[0], size[1]))
    image_surfase.set_colorkey(CLEAR)
    arc(image_surfase, color, (0,0, size[0], size[1]), s_angle, e_angle, width)
    image = image_surfase.convert()
    image.set_alpha(alpha)
    return image

def rotation(scr, im, pos, angle, Flip, zoom=1):
    image1 = py.transform.rotozoom(im, angle, zoom)
    image2 = py.transform.flip(image1, Flip, 0)
    Rect = image2.get_rect(topleft = (pos[0], pos[1]))
    image2.set_colorkey(CLEAR)
    scr.blit(image2, Rect)
    
class cat():
    def __init__(self, position, zoom, body_color, eye_color, ear_color, mirror = 0, alpha = 255):
        self.x = position[0]
        self.y = position[1]
        self.zoom = zoom
        self.body_color = body_color
        self.eye_color = eye_color
        self.ear_color = ear_color
        self.mirror = mirror
        self.alpha = alpha
        pi = 3.14
        
        catx0_size = 400
        caty0_size = 200
        self.cat_size = (catx0_size, caty0_size)
    
        self.head_x = 50
        self.head_y = 50
        self.head_rad0 = 40
        self.head_size = (self.head_rad0 + 10, self.head_rad0 + 10)
        
        self.body_x = 155
        self.body_y = 65
        self.body_size = (290, 110)
        
        self.left_eye_x = 35
        self.left_eye_y = 43
        self.right_eye_x = 65
        self.right_eye_y = self.left_eye_y
        self.eye_size = (25, 30)
        
        self.left_ear_x = 10
        self.left_ear_y = 0
        self.right_ear_x = 60
        self.right_ear_y = self.left_ear_y
        self.ear_size = (23, 23)
        
        self.tail_x = 300
        self.tail_y = 80
        self.tail_size = (130, 25)
        
        self.frontright_leg_x = 20
        self.frontright_leg_y = 100
        self.frontright_leg_size = (35, 45)
        
        self.frontleft_leg_x = 100
        self.frontleft_leg_y = 120
        self.frontleft_leg_size = (60, 37)
        
        self.back_leg1_x = 250
        self.back_leg1_y = 100
        self.back_leg1_size = (50, 50)
        
        self.back_leg2_x = 270
        self.back_leg2_y = 130
        self.back_leg2_size = (20, 50)
        
        self.nose_x = 47
        self.nose_y = 60
        self.nose_size = (10, 10)
        
        self.mouth1_x = 52
        self.mouth1_y = self.nose_y+3
        self.mouth1_rect = (self.mouth1_x, self.mouth1_y, 10, 15)
        self.mouth_width = 1
        self.mouth1_start_angle = pi
        self.mouth1_end_angle = pi*(7/4-1/7)
        
        self.mouth2_x = 42
        self.mouth2_y = self.nose_y+3
        self.mouth2_rect = (self.mouth2_x, self.mouth2_y, 10, 15)
        self.mouth2_end_angle = 2*pi
        self.mouth2_start_angle = pi*(1+7/16)
        
        pass
    
    def cat_draw(self):
        cat_surfase = py.Surface(self.cat_size)               
        cat_surfase.set_colorkey(CLEAR)
        
        RotatedEllipse(cat_surfase, (self.frontright_leg_x, self.frontright_leg_y),    #front right leg
                       self.frontright_leg_size, self.body_color)
        
        RotatedEllipse(cat_surfase, (self.tail_x, self.tail_y),                 #tail
                       self.tail_size, self.body_color, -35)
        
        RotatedEllipse(cat_surfase, (self.body_x, self.body_y),          # body
                       self.body_size, self.body_color)
        
        circle(cat_surfase, self.body_color, (self.head_x, self.head_y),  #head
               self.head_rad0)
        circle(cat_surfase, lightBLACK, (self.head_x, self.head_y), 
               self.head_rad0, 1)
        
        RotatedEllipse(cat_surfase, (self.left_eye_x, self.left_eye_y),            #left eye
                       self.eye_size, self.eye_color)
        RotatedEllipse(cat_surfase, (self.left_eye_x+5, self.left_eye_y), 
                       (8, 25), lightBLACK)
        RotatedEllipse(cat_surfase, (self.left_eye_x-3, self.left_eye_y-7), 
                       (15,10), WHITE, 135)
        
        RotatedEllipse(cat_surfase, (self.right_eye_x, self.right_eye_y),           #right eye
                       self.eye_size, self.eye_color)
        RotatedEllipse(cat_surfase, (self.right_eye_x+5, self.right_eye_y), 
                       (8, 25), lightBLACK)
        RotatedEllipse(cat_surfase, (self.right_eye_x-3, self.right_eye_y-7), 
                       (15,10), WHITE, 135)
        
        RotatedTriangle(cat_surfase, (self.left_ear_x, self.left_ear_y), 
                        self.ear_size, self.ear_color, 215)                      #left ear
        RotatedTriangle(cat_surfase, (self.right_ear_x, self.right_ear_y), 
                        self.ear_size, self.ear_color, 145)                      #right ear
        
        RotatedEllipse(cat_surfase, (self.frontleft_leg_x, self.frontleft_leg_y),    #front left leg
                       self.frontleft_leg_size, self.body_color)
        
        RotatedEllipse(cat_surfase, (self.back_leg1_x, self.back_leg1_y), 
                       self.back_leg1_size, self.body_color)
        
        RotatedEllipse(cat_surfase, (self.back_leg2_x, self.back_leg2_y), 
                       self.back_leg2_size, self.body_color)
        
        RotatedTriangle(cat_surfase, (self.nose_x, self.nose_y), 
                        self.nose_size, self.ear_color, 0, 1)
        
        arc(cat_surfase, lightBLACK,  self.mouth1_rect, self.mouth1_start_angle, 
            self.mouth1_end_angle, self.mouth_width)
        
        arc(cat_surfase, lightBLACK,  self.mouth2_rect, self.mouth2_start_angle, 
            self.mouth2_end_angle, self.mouth_width)
        
        Arc1 = arc_image((70,30), lightBLACK, pi/3, pi*3/4, 1)
        
        rotation(cat_surfase, Arc1, (50, 60), 0, 0) 
        rotation(cat_surfase, Arc1, (50-3, 63), -5, 0)
        rotation(cat_surfase, Arc1, (50-6, 66), -10, 0)
        
        rotation(cat_surfase, Arc1, (-17, 60), 0, 1) 
        rotation(cat_surfase, Arc1, (-17, 63), -5, 1)
        rotation(cat_surfase, Arc1, (-17, 66), -10, 1)
        
        image = cat_surfase.convert()
        image.set_alpha(self.alpha)
        new_surfase = py.transform.flip(cat_surfase, self.mirror, 0)
        image = py.transform.rotozoom(new_surfase, 0, self.zoom)
        Rect = image.get_rect(topleft = (self.x, self.y))
        image.set_colorkey(CLEAR)
        screen.blit(image, Rect)
        pass

def window(pos, size, street_color = BLUE, w_color = WHITE, alpha = 255):
    width = 100
    height = 150
    window_size = (width, height)
    
    window_surfase = py.Surface(window_size)               
    window_surfase.set_colorkey(CLEAR)
    
    rect(window_surfase, w_color, (0, 0, width, height))
    rect(window_surfase, street_color, (4, 4, 43, 44))
    rect(window_surfase, street_color, (53, 4, 43, 44))
    rect(window_surfase, street_color, (4, 57, 43, 88))
    rect(window_surfase, street_color, (53, 57, 43, 88))
    
    image = window_surfase.convert()
    image.set_alpha(alpha)
    image = py.transform.rotozoom(window_surfase, 0, size)
    Rect = image.get_rect(topleft = (pos[0], pos[1]))
    image.set_colorkey(CLEAR)
    screen.blit(image, Rect)
    
def clew(pos, size, c_color = GRAY, alpha = 255):
    rad = 40
    clew_width = 140
    clew_height = 90
    clew_size = (clew_width, clew_height)
    
    clew_surfase = py.Surface(clew_size)               
    clew_surfase.set_colorkey(CLEAR)
    
    circle(clew_surfase, c_color, (45, 45), rad)
    circle(clew_surfase, lightBLACK, (45, 45), rad, 1)
    
    Arc1 = arc_image((80, 80), lightBLACK, 0, pi/2, 1)
    Arc2 = arc_image((88,88), lightBLACK, 0, pi/2, 1)  
    Arc3 = arc_image((65,65), lightBLACK, 0, pi*3/4, 1)
    Arc4 = arc_image((80,80), lightBLACK, pi*4/7, pi*7/8, 1)
    rotation(clew_surfase, Arc1, (0, 10), 0, 0) 
    rotation(clew_surfase, Arc2, (-15, 13), 0, 0)
    rotation(clew_surfase, Arc3, (0, 20), 0, 0)
    
    rotation(clew_surfase, Arc4, (13, 28), 0, 0) 
    rotation(clew_surfase, Arc4, (17, 37), 0, 0)
    rotation(clew_surfase, Arc4, (23, 45), 0, 0)
    
    image = clew_surfase.convert()
    image.set_alpha(alpha)
    image = py.transform.rotozoom(clew_surfase, 0, size)
    Rect = image.get_rect(topleft = (pos[0], pos[1]))
    image.set_colorkey(CLEAR)
    screen.blit(image, Rect)
    
rect(screen, brown, (0, 0, screen_X, wall_height))    
rect(screen, rosybrown5, (0, wall_height, screen_X, screen_X - wall_height))  
window(window_pos, window_size, BLUE)
window((150, 50), window_size, BLUE)
cat(cat_pos, cat_zoom, darkorange3, GREEN, sandybrown, 0).cat_draw()
clew(clew_pos, clew_size, GRAY)

py.display.update()
clock = py.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            finished = True

py.quit()