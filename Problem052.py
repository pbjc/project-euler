#===============================================================================
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#===============================================================================
n = 1
while True:
    d2 = sorted(str(n * 2))
    for i in range(3, 7):
        if sorted(str(n * i)) == d2:
            if i == 6:
                print(n)
                exit()
        else:
            break
    n += 1