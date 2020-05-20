"""
Project Euler Problem 9
"""

possible_tuples = []
actual_tuple = ()

"""First note that as a < b < c and a + b + c = 1000 we know a < 334 and hence a < b < 1000 - 2*a. """

for a in range(1, 334):
    for b in range(a, 1000 - 2*a):
            possible_tuples.append( (a, b, 1000 - a - b ) )

for tup in possible_tuples:
    if tup[0]**2 + tup[1]**2 == tup[2]**2:
        actual_tuple = tup

print( actual_tuple )
print( actual_tuple[0]*actual_tuple[1]*actual_tuple[2] )