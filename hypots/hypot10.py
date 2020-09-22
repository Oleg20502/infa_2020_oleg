#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:09:29 2020

@author: student
"""
import turtle
turtle.shape('turtle')
n = 6

def circle(x):
    turtle.speed(3000)
    n = 180
    fi = 360/n
    step = 3.14*fi*x/180
    for i in range(n):
        turtle.forward(step)
        turtle.left(fi)

for i in range(n):
    circle(70)
    turtle.left(360/n)
turtle.reset()