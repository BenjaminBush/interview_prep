from classes.Graph import *

def detectCycleUtil(graph, curr_node, visited, recursionStack):
	visited[curr_node] = True
	recursionStack[curr_node] = True

	for neighbor in graph[curr_node]:
		if visited[neighbor] == False:
			if detectCycleUtil(graph, neighbor, visited, recursionStack):
				return True
		if recursionStack[neighbor]:
			return True
	return False

def detectCycle(graph):
	visited = [False]*len(graph.items())
	recursionStack = [False]*len(graph.items())
	for node in range(len(graph.items())):
		if visited[node] == False:
			if detectCycleUtil(graph, node, visited, recursionStack):
				return True
	return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if detectCycle(g.graph):
	print("Cycle detected!")
else:
	print("No cycle detected")