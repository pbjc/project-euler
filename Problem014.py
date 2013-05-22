#===============================================================================
# Which starting number, under one million, produces the longest Collatz sequence?
#===============================================================================

cache = {1:1}

def collatzlen(n):
    if n in cache:
        return cache[n]
    elif n % 2 == 0:
        cache[n] = collatzlen(n / 2) + 1
        return cache[n]
    else:
        cache[n] = collatzlen(3 * n + 1) + 1
        return cache[n]

high = 1
highindex = 1
for i in range(1, 1000000):
    length = collatzlen(i)
    if length > high:
        high = length
        highindex = i
print(highindex)