#===============================================================================
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#===============================================================================

def getMonthLength(m, y):
    if m == 2:
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    return 29
                return 28
            return 29
        return 28
    if m in [4, 6, 9, 11]:
        return 30
    return 31         

count = 0
totalDays = 0
day = 1
month = 1
year = 1900
while year <= 2000:
    if year >= 1901 and totalDays % 7 == 6 and day == 1:
        count += 1
    totalDays += 1
    day += 1
    if getMonthLength(month, year) == day - 1:
        if month == 12:
            year += 1
            month = day = 1
        else:
            month += 1
            day = 1
print(count)