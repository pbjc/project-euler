#===============================================================================
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
#===============================================================================

from Common import primeSieve, isPrime

bound = 1000000
primes = list(primeSieve(bound))
length = len(primes)

long = primes[0]
prime = 0
for i in range(length):
    total = primes[i]
    j = i + 1
    while total < bound and j < length:
        total += primes[j]
        if isPrime(total) and j - i + 1 > long:
            long = j - i + 1
            prime = total
        j += 1
print(prime)