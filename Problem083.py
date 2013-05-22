#===============================================================================
# Find the minimal path sum in matrix.txt, a 31K text file containing an 80 by 80 matrix,
# from the top left to the bottom right by moving up, down, left, and right.
#===============================================================================

class Node:

    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.cost = float("inf")
        self.prev = None

mat = open('matrix.txt').read()
layers = mat.split('\n')

unvisited = set()
grid = []

for i in range(len(layers)):
    numList = layers[i].split(',')
    grid.append([])
    for j in range(len(numList)):
        grid[i].append(Node(int(numList[j])))
        if i - 1 >= 0:
            grid[i][j].neighbors.add(grid[i - 1][j])
            grid[i - 1][j].neighbors.add(grid[i][j])
        if j - 1 >= 0:
            grid[i][j - 1].neighbors.add(grid[i][j])
            grid[i][j].neighbors.add(grid[i][j - 1])
        unvisited.add(grid[i][j])

grid[0][0].cost = 0

currNode = None
while len(unvisited - set()) > 0:
    low = float("inf")
    for node in unvisited:
        if node.cost < low:
            low = node.cost
            currNode = node
    if currNode == grid[len(grid) - 1][len(grid) - 1]:
        break
    unvisited.remove(currNode)
    for adj in currNode.neighbors:
        dist = currNode.cost + adj.val
        if dist < adj.cost:
            adj.cost = dist
            adj.prev = currNode

minPathSum = 0
while not currNode == None:
    minPathSum += currNode.val
    currNode = currNode.prev
print(minPathSum)