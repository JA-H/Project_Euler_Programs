import numpy as np 

numbers = np.loadtxt(fname = "p13_number.txt", dtype ="str")
sum = 0

for n in numbers:
    sum += int( n[:15] ) 

digit = str(sum)

print( digit[:10] )