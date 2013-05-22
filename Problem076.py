#===============================================================================
# How many different ways can one hundred be written as a sum of at least two positive integers?
#===============================================================================

def findNumCombos(total, pieces):
    if total == 0:
        return 1
    if len(pieces) == 0 or total < 0:
        return 0
    return findNumCombos(total - pieces[0], pieces) + findNumCombos(total, pieces[1:])

print(findNumCombos(100, list(range(1, 100))))