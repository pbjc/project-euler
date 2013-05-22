#===============================================================================
# How many different ways can £2 be made using any number of coins?
#===============================================================================

def findNumCombos(total, pieces):
    if total == 0:
        return 1
    if len(pieces) == 0 or total < 0:
        return 0
    return findNumCombos(total - pieces[0], pieces) + findNumCombos(total, pieces[1:])

print(findNumCombos(200, [200, 100, 50, 20, 10, 5, 2, 1]))