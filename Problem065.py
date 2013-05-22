#===============================================================================
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
#===============================================================================

from fractions import Fraction

digitCache = {1:2, 2:1, 3:2}

def getDigit(n):
    if n in digitCache:
        return digitCache[n]
    if (n - 3) % 3 == 0:
        digitCache[n] = getDigit(n - 3) + 2
    else:
        digitCache[n] = 1
    return digitCache[n]

def buildConvergent(n, end):
    if n == end:
        return getDigit(n)
    return  getDigit(n) + Fraction(1, buildConvergent(n + 1, end))

def getConvergent(n):
    return buildConvergent(1, n)

print(sum([int(d) for d in str(getConvergent(100).numerator)]))