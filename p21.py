def d(n):
    #Sum of proper divisors of n
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

pairs = []

for i in range(1, 10001):
    pairs.append( (i, d(i)) )

amicable_numbers = []

for tup in pairs:
    a = tup[0]
    b = tup[1]
    if b < 10000:
        c = pairs[b-1]
    if (a != b) and ( a == c[1] ):
        amicable_numbers.append(a)

print( sum(amicable_numbers) )