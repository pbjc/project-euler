#===============================================================================
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#===============================================================================

print(sum([n for n in range(1, 1000000) if str(n) == str(n)[::-1] and str(bin(n))[2:] == str(bin(n))[:1:-1]]))