#===============================================================================
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#===============================================================================

print(sum([i for i in range(10, 1000000) if sum([int(d) ** 5 for d in str(i)]) == i]))