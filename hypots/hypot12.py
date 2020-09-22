#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:30:04 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 6
r1 = 50
r2 = 10
def bow(x):
    turtle.speed(3000)
    n = 180
    fi = 180/n
    step = 3.14*fi*x/180
    for i in range(n):
        turtle.forward(step)
        turtle.right(fi)

turtle.left(90)
for i in range(n):
    bow(r1)
    bow(r2)
turtle.reset()