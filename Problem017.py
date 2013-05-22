#===============================================================================
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#===============================================================================

words = {}
words[1] = 'one'
words[2] = 'two'
words[3] = 'three'
words[4] = 'four'
words[5] = 'five'
words[6] = 'six'
words[7] = 'seven'
words[8] = 'eight'
words[9] = 'nine'
words[10] = 'ten'
words[11] = 'eleven'
words[12] = 'twelve'
words[13] = 'thirteen'
words[14] = 'fourteen'
words[15] = 'fifteen'
words[16] = 'sixteen'
words[17] = 'seventeen'
words[18] = 'eighteen'
words[19] = 'nineteen'
words[20] = 'twenty'
words[30] = 'thirty'
words[40] = 'forty'
words[50] = 'fifty'
words[60] = 'sixty'
words[70] = 'seventy'
words[80] = 'eighty'
words[90] = 'ninety'
words[100] = 'one hundred'

def numToWord(n):
    word = ''
    if n <= 100:
        if n % 10 == 0 or n <= 20:
            word = words[n]
        else:
            word = words[n // 10 * 10] + '-' + words[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            word = words[n // 100] + ' hundred'
        else:
            word = words[n // 100] + ' hundred and ' + numToWord(n % 100)
    else:
        word = 'one thousand'
    return word

print(sum([len(numToWord(i).replace('-', '').replace(' ', '')) for i in range(1, 1001)]))