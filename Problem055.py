#===============================================================================
# How many Lychrel numbers are there below ten-thousand?
#===============================================================================

def isLychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

print(sum([1 for i in range(1, 10000) if isLychrel(i)]))