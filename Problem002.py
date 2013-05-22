#===============================================================================
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#===============================================================================

a, b, total = 0, 1, 0
while b < 4000000:
    if b % 2 == 0:
        total += b
    b += a
    a = b - a
print(total)