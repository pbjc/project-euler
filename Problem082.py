#===============================================================================
# Find the minimal path sum in matrix.txt, a 31K text file containing an 80 by 80 matrix,
# from the left column to the right column by only moving up, down, and right.
#===============================================================================

class Node:

    def __init__(self, val, right, down, up):
        self.val = val
        self.right = right
        self.down = down
        self.up = up
        self.minpath = -1
        self.locked = False

def getMinPath(node):
    node.locked = True
    if node.minpath == -1:
        dirs = []
        if not (node.right == None or node.right.locked):
            dirs.append(getMinPath(node.right))
        if not (node.down == None or node.down.locked):
            dirs.append(getMinPath(node.down))
        if not node.up == None:
            dirs.append(getMinPath(node.up))
        node.minpath = node.val
        if len(dirs) and not node.right == None:
            node.minpath += min(dirs)
    node.locked = False
    return node.minpath

mat = open('matrix.txt').read()
layers = mat.split('\n')
grid = []

for i in range(len(layers)):
    numList = layers[i].split(',')
    grid.append([])
    for j in range(len(numList)):
        grid[i].append(Node(int(numList[j]), None, None, None))
        if i - 1 >= 0:
            grid[i - 1][j].down = grid[i][j]
            grid[i][j].up = grid[i - 1][j]
        if j - 1 >= 0:
            grid[i][j - 1].right = grid[i][j]

print(min([getMinPath(grid[i][0]) for i in range(len(grid))]))