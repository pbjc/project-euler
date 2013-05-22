#===============================================================================
# Considering quadratics of the form:
# 
# n^2 + an + b, where |a| < 1000 and |b| < 1000
# 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.
#===============================================================================

from Common import isPrime, prod

highStreak = 0
coefficients = []
for a in range(-999, 1000):
    for b in range(-999, 1000):
        count = 0
        n = 0
        while isPrime(n ** 2 + a * n + b):
            count += 1
            n += 1
        if count > highStreak:
            highStreak = count
            coefficients = [a, b]
print(prod(coefficients))