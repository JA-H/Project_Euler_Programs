"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 6: https://projecteuler.net/problem=6

@author: John
"""

squares_sum = 0
sum_of_numbers = 0

for i in range(100):
  i += 1
  squares_sum += i*i
  sum_of_numbers += i

print(squares_sum )
print(sum_of_numbers)

print( sum_of_numbers**2 - squares_sum )
