#===============================================================================
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
#===============================================================================

from Common import pentagonnum as p

def isPenta(n):
    return (24 * n + 1) ** .5 % 1 == 0 and (24 * n + 1) ** .5 % 6 == 5

for i in range(1, 10000):
    for j in range(1, i):
        a = p(i)
        b = p(j)
        if isPenta(a - b) and isPenta(a + b):
            print(a - b)
            exit()