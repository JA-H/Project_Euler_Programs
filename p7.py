"""
Created on Wed Apr 15 16:53:36 2020

Project Euler Problem 7: https://projecteuler.net/problem=7

@author: John
"""

def find_Nth_prime(N = 6):
    counter = 2
    primes = [2]
    while len(primes) < N:
      counter += 1
      is_prime = True
      for p in primes:
        if counter % p == 0:
          is_prime = False
          break

      if is_prime == True:
        primes.append(counter)

    print(primes[N-1] )

find_Nth_prime(10001)
