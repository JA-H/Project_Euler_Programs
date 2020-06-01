"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 1: https://projecteuler.net/problem=1

@author: John
"""

def divisible_three_five(n):
    return [x for x in range(1,n) if x%3==0 or x%5==0]

x = sum(divisible_three_five(10001))

print(x)