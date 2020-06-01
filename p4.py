# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 4: https://projecteuler.net/problem=4

@author: John
"""

def is_palindrome(number):
    palindrome = True
    string_number = str(number)
    length_of_number = len(string_number)
    for i in range( length_of_number // 2 ):
        if string_number[i] != string_number[ -1 -i]:
            palindrome = False
            break
    return palindrome

largest_palindrome = 0

for i in range(1000):
    for j in range(1000):
        num = i*j
        if (is_palindrome(num) == True) and (num > largest_palindrome) :
            largest_palindrome = num

        
print( largest_palindrome )