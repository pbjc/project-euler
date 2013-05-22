#===============================================================================
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
# 
# How many routes are there through a 20x20 grid?
#===============================================================================

grid = []
gridlen = 21    #Each node represents a vertice on the grid. So, a length of 3 represents a 2 x 2 grid.

for r in range(gridlen):
    grid.append([])
    for c in range(gridlen):
        grid[r].append(0)

grid[0][0] = 1
for r in range(gridlen):
    for c in range(gridlen):
        if c < gridlen - 1:
            grid[r][c + 1] += grid[r][c]
        if r < gridlen - 1:
            grid[r + 1][c] += grid[r][c]
print(grid[gridlen - 1][gridlen - 1])