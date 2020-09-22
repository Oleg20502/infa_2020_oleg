#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:29:47 2020

@author: student
"""

import turtle as t
import random as r

xc = 10
yc = 10
#turtle.shape('turtle')

for i in range(1000):
  t.goto(xc, yc)
  xc = r.randint(-50, 50) + t.xcor()
  yc = r.randint(-50, 50) + t.ycor()
  #turtle.forward(step)
  #turtle.left(angle)