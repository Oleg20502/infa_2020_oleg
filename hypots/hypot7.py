#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:10:31 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 10000
step = 5
fi = 10
for i in range(n):
    step += 0.2
    #fi *= 1.1
    turtle.forward(step)
    turtle.left(fi)