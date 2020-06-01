N = 2**1000

string_N = str(N)
total = 0

for i in range(len(string_N)):
    total += int( string_N[i] )

print(total)
