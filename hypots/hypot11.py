#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:21:59 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 6
r = 50
step = 10
def circle(x):
    turtle.speed(3000)
    n = 180
    fi = 360/n
    step = 3.14*fi*x/180
    for i in range(n):
        turtle.forward(step)
        turtle.left(fi)

turtle.left(90)
for i in range(n):
    circle(r)
    turtle.left(180)
    circle(r)
    turtle.left(180)
    r += step
turtle.reset()