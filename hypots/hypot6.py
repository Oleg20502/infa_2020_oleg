#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:05:20 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 8
side = 100
for i in range(n):
    turtle.forward(side)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(side)
    turtle.right(180 - 360/n)