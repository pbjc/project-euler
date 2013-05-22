#===============================================================================
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#===============================================================================

from Common import primeSieve
from bisect import bisect_left

def genDoubleSquares(bound):
    for i in range(1, bound):
        yield i ** 2 * 2

def oddCompositeSieve(bound):
    sieve = [True] * bound
    sieve[0] = sieve[1] = False
    for (i, prime) in enumerate(sieve):
        if prime:
            for n in range(i * i, bound, i):
                sieve[n] = False
        elif i % 2 == 1 and i > 1:
            yield i

bound = 10000
primes = list(primeSieve(bound))
doubleSquares = list(genDoubleSquares(bound))
for i in oddCompositeSieve(bound):
    summable = False
    for j in primes[:bisect_left(primes, i)]:
        for k in doubleSquares[:bisect_left(doubleSquares, i)]:
            if j + k == i:
                summable = True
                break
        if summable:
            break
    if not summable:
        print(i)
        break