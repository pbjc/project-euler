#===============================================================================
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#===============================================================================

from Common import isPrime, primeSieve

def isTruncatablePrime(n):
    if n <= 7:
        return False
    s = str(n)
    length = len(s)
    for i in range(length):
        if not isPrime(int(s[i:])):
            return False
    for i in range(length):
        if not isPrime(int(s[:length - i])):
            return False
    return True

print(sum([i for i in primeSieve(1000000) if isTruncatablePrime(i)]))