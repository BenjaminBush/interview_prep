from classes.Graph import *
from queue import Queue

def bfs(graph, source, sink):
	fringe = Queue()
	fringe.put(source)
	visited = []

	while not fringe.empty():
		curr_node = fringe.get()
		visited.append(curr_node)

		# Return
		if curr_node == sink:
			return visited

		for neighbor in graph[curr_node]:
			if neighbor not in visited:
				fringe.put(neighbor)

	return 0

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'E')
g.addEdge('D', 'F')
g.addEdge('D', 'G')
g.addEdge('E', 'H')
g.addEdge('F', 'G')
g.addEdge('F', 'H')
g.addEdge('G', 'H')

print(bfs(g.graph, 'A', 'H'))