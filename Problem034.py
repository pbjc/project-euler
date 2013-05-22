#===============================================================================
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#===============================================================================

from math import factorial

print(sum([i for i in range(3, 100000) if sum([factorial(int(d)) for d in str(i)]) == i]))