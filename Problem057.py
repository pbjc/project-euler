#===============================================================================
# In the first one-thousand expansions of the continued fraction of the square root of two, 
# how many fractions contain a numerator with more digits than denominator?
#===============================================================================

from fractions import Fraction

cache = {0:0}

def getFractionAt(n):
    if n in cache:
        return cache[n]
    cache[n] = Fraction(1, 2 + getFractionAt(n - 1))
    return cache[n]

count = 0
for i in range(8, 1001):
    frac = Fraction(1 + getFractionAt(i))
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        count += 1
print(count)