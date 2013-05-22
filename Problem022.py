#===============================================================================
# What is the total of all the name scores in the file?
#===============================================================================

def getScore(name, ind):
    score = sum([ord(c) - ord('A') + 1 for c in name])
    return score * ind

names = sorted(eval('[' + open('names.txt').read() + ']'))

i = 1
total = 0
for name in names:
    total += getScore(name, i)
    i += 1
print(total)