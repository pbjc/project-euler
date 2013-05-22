#===============================================================================
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
#===============================================================================

from decimal import Decimal, getcontext

getcontext().prec = 102

print(sum([sum([int(d) for d in str(Decimal(i).sqrt())[:101] if not d == '.']) for i in range(1, 101) if not i ** .5 % 1 == 0]))