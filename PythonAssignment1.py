#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:51:43 2021

@author: bhavinpatel
"""

#Problem 1
def problem1():
   
    L = []
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            L.append(i)
    print(*L, sep = ", ")

problem1()



#Problem 2
def problem2(first, last):
    
    print(first[::-1],",", last[::-1])
    
problem2('Bhavin', 'Patel')


import math
#Problem3
def problem3(r):
    
    V = (4/3) * math.pi * r**3
    print(V)

problem3(12)
