"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 3: https://projecteuler.net/problem=3

@author: John
"""

def largestprimefactor(number):
    largest_prime = 2
    for i in range(2, number):
        while number % i == 0:
            number = number/i
            largest_prime = i
    return largest_prime

print(largestprimefactor(28))