from classes.Node import *
from classes.Tree import *

def findSmallest(node):
	if node is None or node == None:
		return float("inf")

	res = node.data
	lres = findSmallest(node.left)
	rres = findSmallest(node.right)

	if res > lres:
		res = lres

	if res > rres:
		res = rres


	return rres

root = generateTree()
printTree(root)
print()
print(findSmallest(root))
