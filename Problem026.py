#===============================================================================
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#===============================================================================

from decimal import Decimal, getcontext

getcontext().prec = 2000

def findCycle(s, prec, bound):
    if len(s) < prec or len(s) < bound:
        return ''
    for i in range(1, prec):
        sub = s[0:i]
        rem = s.replace(sub, '')
        if s[i:].find(sub) == -1 or len(sub) < len(rem) or not s[len(s) - len(rem):] == rem:
            continue
        if len(rem) == 0 or diff(sub, rem) in [0, 1]:
            return sub
    return findCycle(s[1:], prec - 1, bound)
        
def diff(s1, s2):
    r = min(len(s1), len(s2))
    for i in range(r):
        if int(s1[i]) <= int(s2[i]):
            return int(s2[i]) - int(s1[i])
    return -1

high = -1
highindex = 0
for i in range(1, 1000):
    length = len(findCycle(str(1 / Decimal(i))[2:], getcontext().prec, high))
    if length > high:
        high = length
        highindex = i
print(highindex)