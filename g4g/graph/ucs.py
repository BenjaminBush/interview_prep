from classes.Graph import *
from queue import PriorityQueue

def ucs(graph, source, sink):
	fringe = PriorityQueue()
	fringe.put((0, source))
	visited = []

	while not fringe.empty():
		curr_weight, curr_node = fringe.get()
		visited.append(curr_node)

		if curr_node == sink:
			return visited

		for neighbor in graph[curr_node]:
			if neighbor not in visited:
				fringe.put((graph[curr_node][neighbor] + curr_weight, neighbor))

g = WeightedGraph()
g.addEdge('S', 'A', 1)
g.addEdge('S', 'B', 5)
g.addEdge('S', 'C', 15)
g.addEdge('A', 'S', 1)
g.addEdge('A', 'G', 10)
g.addEdge('B', 'S', 5)
g.addEdge('B', 'G', 5)
g.addEdge('C', 'S', 15)
g.addEdge('C', 'G', 5)
g.addEdge('G', 'A', 10)
g.addEdge('G', 'B', 5)
g.addEdge('G', 'C', 5)


print(ucs(g.graph, 'S', 'G'))