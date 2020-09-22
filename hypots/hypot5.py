#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:49:20 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 5
side = 30
width = 10
for i in range(n):
    side += 2*width
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(180)
    turtle.pendown()