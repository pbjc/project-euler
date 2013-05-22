#===============================================================================
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#===============================================================================

from Common import divisors

bound = 28123
abundants = []
[abundants.append(i) for i in range(1, bound) if sum(divisors(i)) - i > i]

sums = set()
high = 0
length = len(abundants)
for i in range(length):
    high = 0
    j = i;
    while high < bound and j < length:
        summed = abundants[i] + abundants[j]
        sums.add(summed)
        high = summed
        j += 1
    if abundants[i] * 2 >= bound:
        break

print(sum(set(range(1, bound)) - sums))