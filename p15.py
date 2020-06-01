product =1

n = 20

for i in range(1, n + 1):
    product *= (n + i)/i

print(round(product))