# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 01:02:05 2019

@author: John
"""

#Project Euler Problem 48

a = 0

for i in range(1, 1000):
    a += i**i 
    a = a % 10**10

print(a)
    