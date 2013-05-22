#===============================================================================
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime,
# and, (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?
#===============================================================================

from Common import primeSieve

cache = {}

for i in primeSieve(10000):
    s = str(i)
    if len(s) == 4:
        ordered = ''.join(sorted(s))
        if ordered in cache:
            cache[ordered].append(i)
        else:
            cache[ordered] = [i]

for k in cache:
    perms = cache[k]
    if len(perms) >= 3:
        diffs = {}
        for i in range(len(perms)):
            for j in range(i + 1, len(perms)):
                diff = perms[j] - perms[i]
                if diff in diffs:
                    if not str(perms[i]) in diffs[diff]:
                        diffs[diff].append(str(perms[i]))
                    diffs[diff].append(str(perms[j]))
                    if len(diffs[diff]) == 3:
                        print(''.join(diffs[diff]))
                        exit()
                else:
                    diffs[diff] = [str(perms[i]), str(perms[j])]