#===============================================================================
# Find the largest palindrome made from the product of two 3-digit numbers.
#===============================================================================

print(max([i * j for j in range(100, 1000) for i in range(j, 1000) if str(i * j) == str(i * j)[::-1]]))