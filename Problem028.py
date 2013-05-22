#===============================================================================
# What is the sum of the numbers on the diagonals in a 1001 by 1001 number spiral?
#===============================================================================

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    
gridlength = 1001      #Odd numbers only
grid = []
for r in range(gridlength):
    grid.append([])
    for c in range(gridlength):
        grid[r].append(0)
r = c = gridlength // 2
d = 0

grid[r][c] = 1
while True:
    if r == 0 and c == gridlength - 1:
        break
    if r < 0 or r >= gridlength or c < 0 or c >= gridlength:
        d = (d + 1) % 4
    if d == RIGHT and grid[r][c + 1] == 0:
        grid[r][c + 1] = grid[r][c] + 1
        c += 1
        d = (d + 1) % 4
    elif d == DOWN and grid[r + 1][c] == 0:
        grid[r + 1][c] = grid[r][c] + 1
        r += 1
        d = (d + 1) % 4
    elif d == LEFT and grid[r][c - 1] == 0:
        grid[r][c - 1] = grid[r][c] + 1
        c -= 1
        d = (d + 1) % 4
    elif d == UP and grid[r - 1][c] == 0:
        grid[r - 1][c] = grid[r][c] + 1
        r -= 1
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4

print(sum([grid[i][i] + grid[gridlength - i - 1][i] for i in range(gridlength)]) - 1)