#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:36:01 2020

@author: student
"""

import turtle
turtle.shape('turtle')
n = 1
r_sm = 80
r_m = 40
r_eye = 10
eye_p = 30
m_w = 7
n_w = 7
n_l = 25
sm_c = 'yellow'
m_c = 'red'
eye_c = 'blue'
f_sm = 1
f_eye = 1

def circle(x, f, c):
    turtle.speed(3000)
    n = 180
    fi = 360/n
    step = 3.14*fi*x/180
    if f == 1:
        turtle.begin_fill()
        turtle.color(c)
    for i in range(n):
        turtle.forward(step)
        turtle.left(fi)
    if f == 1:
        turtle.end_fill()

def bow(x, w, c):
    turtle.speed(3000)
    n = 180
    fi = 180/n
    step = 3.14*fi*x/180
    turtle.width(w)
    turtle.color(c)
    for i in range(n):
        turtle.forward(step)
        turtle.right(fi)

#turtle.left(90)
for i in range(n):
    circle(r_sm, f_sm, sm_c)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(2*r_sm - 30)
    turtle.left(90)
    turtle.forward(eye_p)
    turtle.pendown()
    
    circle(r_eye, f_eye, eye_c)
    
    turtle.penup()
    turtle.left(180)
    turtle.forward(2*eye_p)
    turtle.left(180)
    turtle.pendown()
    
    circle(r_eye, f_eye, eye_c)
    
    turtle.penup()
    turtle.forward(eye_p)
    turtle.left(90)
    turtle.forward(r_sm - 45)
    turtle.pendown()
    
    turtle.width(n_w)
    turtle.forward(n_l)
    
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(r_m)
    turtle.right(90)
    turtle.pendown()
    
    bow(r_m, m_w, m_c)
    
    turtle.penup()












