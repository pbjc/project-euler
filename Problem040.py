#===============================================================================
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1  d10  d100  d1000  d10000  d100000  d1000000
#===============================================================================

from Common import prod

intConcat = ''
n = 0
while len(intConcat) <= 1000000:
    intConcat += str(n)
    n += 1

print(prod([int(intConcat[10 ** i]) for i in range(7)]))