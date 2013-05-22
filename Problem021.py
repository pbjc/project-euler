#==============================================================================
# Evaluate the sum of all the amicable numbers under 10000.
#==============================================================================

from Common import divisors

total = 0
for a in range(1, 10000):
    b = sum(divisors(a)) - a
    if sum(divisors(b)) - b == a and not a == b:
        total += a
print(total)