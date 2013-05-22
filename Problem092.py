#===============================================================================
# How many starting numbers for a square digit chain below ten million will arrive at 89?
#===============================================================================

cache = {1:False, 89:True}

def sqDigitSum(n):
    total = 0
    while n:
        total += (n % 10) ** 2
        n //= 10
    return total

def eightyniner(n):
    if n in cache:
        return cache[n]
    cache[n] = eightyniner(sqDigitSum(n))
    return cache[n]

print(sum([1 for i in range(1, 10 ** 7) if eightyniner(i)]))