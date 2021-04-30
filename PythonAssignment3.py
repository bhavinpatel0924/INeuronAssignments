#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:50:43 2021

@author: bhavinpatel
"""

#Problem 1.1

def add(x, y):
    
    return x + y

def myReduce(function, lst):
    
    count = lst[0]
    for i in lst[1:]:
        
        count = function(count,i)
        
    return count

print(myReduce(add, [1,2,3,4]))



#Problem 1.2

def myFunc(x):
    
    if x >= 18:
        return True
    else:
        return False

ages = [5, 12, 17, 18, 24, 32]
    
def myFilter(function, iterable):
    
    L = []
    for x in iterable:
       if function(x) == True:
           L.append(x)
    return L

hi = myFilter(myFunc, ages)
for i in hi:
    print(i)
    
#Problem 2

print([i*j for i in ['x','y','z'] for j in range(1,5)])

print([i*j for j in range(1,5) for i in ['x','y','z']]) 

print([[i+j] for i in [2,3,4] for j in range(0,3)])

print([[i+j for i in [2,3,4,5]] for j in range(0,4)])

print([(i,j) for i in [1,2,3] for j in [1,2,3]])