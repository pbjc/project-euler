#===============================================================================
# What is the value of the first triangle number to have over five hundred divisors?
#===============================================================================

from Common import divisors, trianglenum

i = 1
while True:
    if len(divisors(trianglenum(i))) > 500:
        break
    i += 1
print(trianglenum(i))