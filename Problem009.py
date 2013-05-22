#===============================================================================
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#===============================================================================
for a in range(1, 1000):
    for b in range(1, a):
        c = (a * a + b * b) ** .5
        if a + b + c == 1000:
            print(int(a * b * c))
            exit()