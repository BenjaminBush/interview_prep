from classes.Graph import *

# MST is tree that connects all nodes in the tree using the minimum possible cost/number of edges
# Psuedocode:
# Randomly select first note v to add to MST
# Choose edge of min cost from MST set to non-MST set

def prim(graph):
	V = []
	T = []
	v1 = '0'
	u1 = '1'
	e1 = graph[v1][u1]
	V.append(v1)

	for i in range(len(graph.items())):
		vi, ui = getMinEdge(graph, V)
		T.append((vi, ui))
		V.append(ui)

	return T

def getMinEdge(graph, V):
	U = []
	for vi in graph:
		if vi not in V:
			U.append(vi)

	min_cost = float("inf")
	ret_v = 0
	ret_u = 0

	for vi in V:
		for ui in U:
			if ui in graph[vi]:
				if graph[vi][ui] < min_cost:
					min_cost = graph[vi][ui]
					ret_v = vi
					ret_u = ui

	return ret_v, ret_u


g = WeightedGraph()
g.addEdge('0', '1', 4)
g.addEdge('0', '7', 8)
g.addEdge('1', '0', 4)
g.addEdge('1', '7', 11)
g.addEdge('1', '2', 8)
g.addEdge('2', '1', 8)
g.addEdge('2', '3', 7)
g.addEdge('2', '5', 4)
g.addEdge('2', '8', 2)
g.addEdge('3', '2', 7)
g.addEdge('3', '4', 9)
g.addEdge('3', '5', 14)
g.addEdge('4', '3', 9)
g.addEdge('4', '5', 10)
g.addEdge('5', '2', 4)
g.addEdge('5', '3', 14)
g.addEdge('5', '4', 10)
g.addEdge('5', '6', 2)
g.addEdge('6', '5', 2)
g.addEdge('6', '7', 1)
g.addEdge('6', '8', 6)
g.addEdge('7', '0', 8)
g.addEdge('7', '1', 11)
g.addEdge('7', '6', 1)
g.addEdge('7', '8', 7)
g.addEdge('8', '2', 2)
g.addEdge('8', '6', 6)
g.addEdge('8', '7', 7)

print(prim(g.graph))
