from classes.Tree import *

def findMaxUtil(root):
	if root is None:
		return 0

	l = findMaxUtil(root.left)
	r = findMaxUtil(root.right)

	max_parent = max(max(l, r) + root.data, root.data)

	max_curr = max(max_parent, l + r + root.data)

	findMaxUtil.res = max(max_parent, max_curr)

	return max_parent

def findMax(root):
	findMaxUtil.res = float("-inf")
	return findMaxUtil(root)

root = generateTree()
printTree(root)
print()
print("Max path is : {}".format(findMax(root)))