#===============================================================================
# What is the largest n-digit pandigital prime that exists?
#===============================================================================

from Common import primeSieve, isPandigital

print(max([i for i in primeSieve(10000000) if isPandigital(i)]))