#===============================================================================
# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
#===============================================================================

from Common import trianglenum

def wordValue(word):
    return sum([ord(c) - ord('A') + 1 for c in word])

trinums = []
for i in range(1, 365):     #The longest word in the file has 14 letters, so the highest possible score is 14 * 26 = 364
    trinums.append(trianglenum(i))
words = sorted(eval('[' + open('words.txt').read() + ']'))

print(sum([1 for word in words if wordValue(word) in trinums]))