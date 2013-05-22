#===============================================================================
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#===============================================================================

from Common import lcm

answer = 1
for i in range(1, 21):
    answer = lcm(i, answer)
print(answer)