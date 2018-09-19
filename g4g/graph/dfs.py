from classes.Graph import *

def dfs(graph, source, sink):
	fringe = [source, ]
	visited = []

	while len(fringe):
		curr_node = fringe.pop()
		visited.append(curr_node)

		if curr_node == sink:
			return visited

		for neighbor in graph[curr_node]:
			if neighbor not in visited:
				fringe.append(neighbor)

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

print(dfs(g.graph, 'A', 'H'))