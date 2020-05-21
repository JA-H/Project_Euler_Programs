from scipy.special import comb

# 9! > 1*10**6 so we only have to check n  \leq 9

print(sum([ int( bool(comb(n, k) > 10**6 ) ) for n in range(1, 101) for k in range(1, n)  ]))