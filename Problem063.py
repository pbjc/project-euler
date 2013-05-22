#===============================================================================
# How many n-digit positive integers exist which are also an nth power?
#===============================================================================

count = 9
for i in range(2, 10):
    for p in range(2, 50):
        if i ** p >= 10 ** (p - 1):
            if i ** p < 10 ** p:
                count += 1
            else:
                break
print(count)