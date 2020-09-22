#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:23:43 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 1000
step = 5
for i in range(n):
    step += 5
    turtle.forward(step)
    turtle.left(90)
turtle.reset()
