#THIS CODE DOES NOT WORK

def number_form(a, b):
        return (a**2)*(b**3)

def F(n):
    number = 0
    a, b = 2, 2
        
    while( number_form(a, b) <= n ):
        number += 1
        if number_form(a + 1, b) <= n:
            a += 1
            break
        elif (number_form(a + 1, b) > n) and (number_form(a, b+1) <= n):
            a = 2
            b += 1
    return number

print(F(32) )

