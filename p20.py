from math import factorial

fac = factorial(100)
sum = 0

while fac != 0:
    end_dig = fac % 10
    sum += end_dig
    fac = (fac - end_dig)//10

print(sum)

