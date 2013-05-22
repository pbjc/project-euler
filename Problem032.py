#===============================================================================
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#===============================================================================

from itertools import permutations

products = set()
pandigitals = list(permutations(range(1, 10)))
for p in pandigitals:
    p = str(p)
    s = p.replace(', ', '').replace('(', '').replace(')', '')
    for i in range(1, 3):
        for j in range(1, 5):
            multiplicand = int(s[:i])
            multiplier = int(s[i:i + j])
            product = int(s[i + j:])
            if multiplicand * multiplier > product:
                break
            if multiplicand * multiplier == product:
                products.add(product)
print(sum(products))