#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:04:31 2021

@author: bhavinpatel
"""
#

#Problem 1
l = ['*']
count = 4
for i in l:
    for j in range(1,7):
        if j != 6:
            print(i*j)
        else:
            for k in sorted(range(4),reverse=True):
                print(i*k)
    

#Problem 2
def reverse(user):
    
    txt = user[::-1]
    return (txt)
    
print(reverse('ineuron'))