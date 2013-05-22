#===============================================================================
# Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?
#===============================================================================

def digitSum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

print(max([digitSum(a ** b) for a in range(100) for b in range(100)]))