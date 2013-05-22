#===============================================================================
# Find the smallest cube for which exactly five permutations of its digits are cube.
#===============================================================================

from bisect import bisect_left

cache = {}
i = 1
while True:
    cube = i ** 3
    ordered = ''.join(sorted(str(cube)))
    if ordered in cache:
        cache[ordered].insert(bisect_left(cache[ordered], cube), cube)
        if len(cache[ordered]) == 5:
            print(cache[ordered][0])
            exit()
    else:
        cache[ordered] = [cube]
    i += 1