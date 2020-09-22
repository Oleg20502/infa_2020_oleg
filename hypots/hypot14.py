#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:22:33 2020

@author: student
"""

import turtle
turtle.shape('turtle')

n = 11
side = 150

def star(n, s):
    turtle.left(180)
    for i in range(n):
         turtle.forward(s)
         turtle.left(180 - 180/n)
star(n, side)