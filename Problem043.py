#===============================================================================
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# 
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.
#===============================================================================

from Common import primeSieve
from itertools import permutations

primes = [0] + list(primeSieve(18))
pandigitals = list(permutations(range(10)))

def isSpecial(n):
    s = str(n)
    for i in range(1, 8):
        sub = s[i] + s[i + 1] + s[i + 2]
        if not int(sub) % primes[i] == 0:
            return False
    return True

total = 0
for t in pandigitals:
    t = str(t).replace(', ', '').replace('(', '').replace(')', '')
    if isSpecial(t):
        total += int(t)
print(total)