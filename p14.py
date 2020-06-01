def Collatz_Sequence(n):
    """Takes a positive integer n and returns the Collatz sequence"""
    m = n
    seq = [m]
    while m > 1 :
        if m % 2 == 0:
            m = m//2
            seq.append(m)
        else:
            m = 3*m + 1
            seq.append( m )
    return seq, len(seq)

longest_Collatz_number = 1
longest_length = 1

for i in range(1, 10**6):
    test = Collatz_Sequence(i)
    if test[1] > longest_length:
        longest_Collatz_number = i
        longest_length = test[1]

print(longest_Collatz_number)
    
