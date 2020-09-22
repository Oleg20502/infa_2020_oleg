#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:55:43 2020

@author: student
"""
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
    d2[A[i]] = A[i+1]
