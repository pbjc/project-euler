#===============================================================================
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
#===============================================================================

from math import factorial as fact

print(sum([1 for n in range(1, 101) for r in range(1, n + 1) if fact(n) // (fact(r) * fact(n - r)) > 10 ** 6]))