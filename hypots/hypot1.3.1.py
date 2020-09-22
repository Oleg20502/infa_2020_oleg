#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:53:01 2020

@author: student
"""

import turtle as t
     
x0, y0 = -300, 0
t.speed(5)

A = []
d1, d2 = {}, {}
with open('Digits_data.txt') as f:
    for i in f:
        a,b = i.split(':')
        A.append(a)
        A.append(b)
print(len(A))
for i in range(0,20,2):
    d1[A[i]] = A[i+1]
for i in range(20, 38, 2):
    d2[A[i]] = list(A[i+1])

def number(a, x, y, d2):
    t.penup()
    t.goto(x, y)
    for i in a:        
        t.goto(x + d2[i][0], y + d2[i][1])
        t.pendown()
        t.goto(x + d2[i][0] + d2[i][2], y + d2[i][1] + d2[i][3])
        t.penup()
        
#n = input()
n = '1234567890'
for i in n:
    number(d1[i], x0, y0, d2)
    x0 += 80
    y0 = 0

    
    
    
    
    
    