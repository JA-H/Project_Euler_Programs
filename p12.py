from prime_generator import *

def Triangle_Num(n):
    #Returns nth triangle number
    return n*(n+1)//2

def Number_of_Factors(n, prime_list):
    #Returns number of factors of a positve integer n given a list of primes
    number_of_factors = 1
    
    for factor in prime_list:
        multiplicity = 1
        while n % factor == 0:
            multiplicity += 1
            n = n // factor
        number_of_factors *= multiplicity
                
    return number_of_factors


primes = Primes(65500)
k = 1

while Number_of_Factors( Triangle_Num(k), primes ) <= 500:
    k += 1

print(Triangle_Num(k))
