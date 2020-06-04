from prime_generator import * 

N = 10000

primes = Primes(N)
squares = [ i**2 for i in range(1, N)]
odd_composite = [ i for i in range(3, N, 2) if (i not in primes) ]

for p in primes:
    for s in squares:
        c = p + 2*s
        if c in odd_composite:
            odd_composite.remove(c)


print(odd_composite)