#===============================================================================
# What is the 10001st prime number?
#===============================================================================

from Common import isPrime

count = 0
i = 1
while True:
    if (isPrime(i)):
        count += 1
        if count == 10001:
            break
    i += 1
print(i) 