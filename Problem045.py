#===============================================================================
# Find the next triangle number that is also pentagonal and hexagonal after 40755.
#===============================================================================

from Common import trianglenum, pentagonnum, hexagonnum

trinums = set()
pentnums = set()
hexnums = set()
for i in range(1, 100000):
    trinums.add(trianglenum(i))
    pentnums.add(pentagonnum(i))
    hexnums.add(hexagonnum(i))
for i in trinums:
    if i > 40755 and i in pentnums and i in hexnums:
        print(i)
        break