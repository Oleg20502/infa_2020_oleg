import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 100
size = np.array([1000, 667])
size_x, size_y = size[0], size[1]

S = np.array([[size_x, 0], [0, size_y]], ndmin=2)

screen = pygame.display.set_mode(size)

def vecmul(vec, k):
    return [vec[0] * k, vec[1] * k]
#Сумма векторов
def vecsum(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1]]
#Факториал
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def fx(k): 
    return round(k * size_x)
def fy(k):
    return round(k * size_y)
#Относительную позицию превращает в абсолютную
def fxy(pos):
    return [fx(pos[0]), fy(pos[1])]
#Применяют fx, fy, fxy к списку значений
def fxm(array):
    return [fx(i) for i in array]
def fym(array):
    return [fy(i) for i in array]
def trans(array):
    coor = array@S
    return coor


'''def beziercurve(pointlist, stepcount=100):
    n = len(pointlist) - 1
    result = [[0, 0]] * stepcount
    for step in range(0, stepcount):
        t = step / (stepcount-1)
        vec = [0, 0]
        for j, pt in enumerate(pointlist):
            vec = vecsum(vec, 
                vecmul(pt,
                    fact(n)/(fact(j)*fact(n-j)) * t**j * (1-t)**(n-j)
                    )
                )
        result[step] = vec
    return result'''

def beziercurve1(pointlist, stepcount=100):
    n = len(pointlist)
    pl = np.array(pointlist)
    result = np.zeros((stepcount, 2))
    for step in range(stepcount):
        t = step / (stepcount-1)
        vec = np.zeros(2)
        for i in range(n):
            vec += np.array(pl[i])*fact(n)/(fact(j)*fact(n-j)) * t**j * (1-t)**(n-j)
        result[step] = vec
    return result

color = [172,67,52]
poly = trans(beziercurve([
        [0.025, 0.520],
        [0.087, 0.321],
        [0.136, 0.355],
        [0.175, 0.640],
        ]))

'''poly = fxym([
        [0.025, 0.520],
        [1.087, 0.321],
        [0.136, 0.355],
        [0.175, 0.640],
         ])'''

polygon(screen, color, poly)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()