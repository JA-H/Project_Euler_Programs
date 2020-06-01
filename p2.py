# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 2: https://projecteuler.net/problem=2

@author: John
"""

def fib(n):
	result = []
	a, b = 0, 1
	while b < n:	
		result.append(b)
		a, b = b, a+b
	return result

even_fib4million = [x for x in fib(4000000) if x % 2 == 0]

print(sum(even_fib4million))