#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:26:53 2020

@author: student
"""

import turtle
import numpy as np
turtle.shape('turtle')
n = 10
m0 = 3
step = 40
r0 = step * np.sin(np.pi*(1 - 2/m0))*2/3
r = r0
width = 15
for i in range(n):
    fi = 180 - 360/m0
    turtle.left(180 - fi/2)
    turtle.forward(step)
    for j in range(m0-1):
        turtle.left(180 - fi)
        turtle.forward(step)
    turtle.penup()
    turtle.right(fi/2)
    turtle.forward(width)
    turtle.pendown()
    m0 += 1
    r += width
    step = 2*np.sin(np.pi/m0)*r
turtle.reset()