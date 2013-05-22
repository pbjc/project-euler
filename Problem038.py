#===============================================================================
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
#===============================================================================

from Common import isPandigital

def repeatsDigits(n):
    s = str(n)
    for d in s:
        s = s.replace(d, '', 1)
        if d in s:
            return True
    return False

i = 9999
while True:
    s = ''
    k = 1
    while True:
        s = s + str(i * k)
        if repeatsDigits(s) or int(s) > 987654321:
            break
        elif isPandigital(s):
            print(s)
            exit()
        k += 1
    i -= 1