#===============================================================================
# What is the largest prime factor of the number 600851475143 ?
#===============================================================================

from Common import isPrime, divisors

print(max([i for i in divisors(600851475143) if isPrime(i)]))