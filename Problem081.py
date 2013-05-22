#===============================================================================
# Find the minimal path sum in matrix.txt, a 31K text file containing an 80 by 80 matrix,
# from the top left to the bottom right by only moving right and down.
#===============================================================================

class Node:

	def __init__(self, val, right, down):
		self.val = val
		self.right = right
		self.down = down
		self.minpath = -1

def getMinPath(node):
	if node.minpath == -1:
		dirs = []
		if not node.right == None:
			dirs.append(getMinPath(node.right))
		if not node.down == None:
			dirs.append(getMinPath(node.down))
		node.minpath = node.val
		if len(dirs):
			node.minpath += min(dirs)
	return node.minpath

mat = open('matrix.txt').read()
layers = mat.split('\n')
grid = []

for i in range(len(layers)):
	numList = layers[i].split(',')
	grid.append([])
	for j in range(len(numList)):
		grid[i].append(Node(int(numList[j]), None, None))
		if i - 1 >= 0:
			grid[i - 1][j].down = grid[i][j]
		if j - 1 >= 0:
			grid[i][j - 1].right = grid[i][j]

print(getMinPath(grid[0][0]))