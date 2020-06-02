def Fibonacci():
    u0, u1 = 1, 1
    yield u0
    yield u1
    while True:
        u0, u1 = u1, u0 + u1
        yield u1

index = 1

for fib in Fibonacci():
    if fib < 10**999:
        index += 1
    else:
        break
        

print(index)