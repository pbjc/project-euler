#===============================================================================
# How many circular primes are there below one million?
#===============================================================================

from Common import isPrime, primeSieve

def isCircularPrime(n):
    s = str(n)
    for i in range(len(s)):
        if not isPrime(int(s[i:] + s[:i])):
            return False
    return True

print(len([i for i in primeSieve(1000000) if isCircularPrime(i)]))