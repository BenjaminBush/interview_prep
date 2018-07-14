from queue import Queue, PriorityQueue


def bfs(graph, start, end):
    fringe = Queue()
    fringe.put(start)
    visited = []

    while not fringe.empty():
        current_node = fringe.get()
        visited.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return visited

        for node in graph[current_node]:
            if node not in visited:
                fringe.put(node)


def dfs(graph, start, end):
    fringe = [start, ]
    visited = []

    while len(fringe):
        current_node = fringe.pop()
        visited.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return visited

        # expanding nodes
        for node in reversed(graph[current_node]):
            if node not in visited:
                fringe.append(node)


def ucs_weight(from_node, to_node, weights=None):
    """
    Returns the UCS weight for a edge between from and to
    """
    return weights.get((from_node, to_node), 10e100) if weights else 1


def ucs(graph, start, end, weights=None):
    """
    Function to compute UCS(Uniform Cost Search) for a graph
    """
    fringe = PriorityQueue()
    fringe.put((0, start))  # (priority, node)
    visited = []

    while not fringe.empty():
        curr_weight, current_node = fringe.get()
        visited.append(current_node)

        if current_node == end:
            return visited

        for node in graph[current_node]:
            if node not in visited:
                fringe.put((
                    curr_weight + ucs_weight(current_node, node, weights),
                    node
                ))


if __name__ == "__main__":
    first_graph = {
    	'A' : ['B', 'C'],
    	'B' : ['D'],
    	'C' : ['E'],
    	'D' : ['F', 'G'],
    	'E' : ['H'],
    	'F' : ['G', 'H'],
    	'G' : ['H'],
    	'H' : []
    }

    print(bfs(first_graph, 'A', 'H'))
    print(dfs(first_graph, 'A', 'H'))
    print(ucs(first_graph, 'A', 'H'))

    ucs_test_graph = {
        'S': ['A', 'B', 'C'],
        'A': ['S', 'G'],
        'B': ['S', 'G'],
        'C': ['S', 'G'],
        'G': ['A', 'B', 'C']
    }

    ucs_test_weight = {
        ('S', 'A'): 1,
        ('S', 'B'): 5,
        ('S', 'C'): 15,
    
        ('A', 'G'): 10,
        ('A', 'S'): 1,
    
        ('B', 'S'): 5,
        ('B', 'G'): 5,
    
        ('C', 'S'): 15,
        ('C', 'G'): 5,
    
        ('G', 'A'): 10,
        ('G', 'B'): 5,
        ('G', 'C'): 5,
    }
    print(ucs(ucs_test_graph, 'S', 'G', ucs_test_weight))