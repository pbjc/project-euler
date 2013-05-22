#===============================================================================
# Find the maximum total from top to bottom of the triangle below
#===============================================================================

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.maxpath = -1

def getMaxPath(node):
    if node == None:
        return 0
    if node.maxpath == -1:
        node.maxpath = max(getMaxPath(node.left), getMaxPath(node.right)) + node.val
    return node.maxpath

triangle = open('triangle.txt').read()
layers = triangle.split('\n')
grid = []

for i in range(len(layers)):
    numList = layers[i].split(' ')
    grid.append([])
    for j in range(len(numList)):
        grid[i].append(Node(int(numList[j]), None, None))
        if i - 1 >= 0:
            if j < len(grid[i - 1]):
                grid[i - 1][j].left = grid[i][j]
            if j - 1 >= 0 and j - 1 < len(grid[i - 1]):
                grid[i - 1][j - 1].right = grid[i][j]

print(getMaxPath(grid[0][0]))