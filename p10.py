def PrimeSum(n):
    """Calculates the sum of all the primes less than or equal to n."""
    prime = [True for i in range(n + 1)]
    p = 2
    while( p*p <= n ):
        if (prime[p] == True):
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    
    prime[0], prime[1] = False, False

    prime_sum = 0

    for p in range(n + 1):
        if prime[p]:
            prime_sum += p 
    return prime_sum

print( PrimeSum(2*(10**6)) )