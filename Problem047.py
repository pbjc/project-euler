#===============================================================================
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
#===============================================================================

from Common import isPrime, divisors

def distinctPrimeFactors(n):
    div = divisors(n)
    div.remove(1)
    toRemove = set()
    [toRemove.add(d) for d in div if not isPrime(d)]
    return div - toRemove

i = 647
while True:
    if len(distinctPrimeFactors(i)) == 4:
        for j in range(1, 4):
            if len(distinctPrimeFactors(i + j)) == 4:
                if j == 3:
                    print(i)
                    exit()
            else:
                break
        else:
            i += j
    i += 1