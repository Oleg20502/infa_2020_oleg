#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:40:38 2020

@author: student
"""
import turtle
n = 1000
step = 1000/n
for i in range(n):
    turtle.shape('turtle')
    turtle.forward(step)
    turtle.left(360/n)
