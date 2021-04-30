#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:32:50 2021

@author: bhavinpatel
"""

#Problem 1.1
class Parent():
    
    def __init__(self, base, height):
        
        self.base = base
        self.height = height
    
    def area(self):
        
        return self.base * self.height * .5
    

area1 = Parent(3,2)
print(area1.area())



#Problem 1.2
def filter_long_words(lst, n):
    
    for i in lst:
        if len(i) <= n:
            print(i)
filter_long_words(['hi','bhavin', 'ineuron', 'basketball'], 6)



#Problem 2.1
def length_of_words(lst):
    
    L = []
    for i in lst:
        n = len(i)
        L.append(n)
    print(L)

length_of_words(['ab','cde', 'erty'])



#Problem 2.2
def char(character):
    
    L = ['a','e','i','o','u']
    
    if character in L:
        print(True)
    else:
        print(False)
        
char('a')