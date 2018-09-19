from collections import defaultdict

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)

class WeightedGraph(Graph):
	def __init__(self):
		self.graph=defaultdict(dict)
	def addEdge(self, u, v, weight):
		self.graph[u][v] = weight