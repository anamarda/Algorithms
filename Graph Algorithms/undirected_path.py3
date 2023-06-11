# undirected path
# Write a function, undirected_path, that takes in an array of edges for an undirected graph 
# and two nodes (nodeA, nodeB). The function should return a boolean indicating whether or not 
# there exists a path between nodeA and nodeB.


def undirected_path(edges: list, nodeA: str, nodeB: str) -> bool:
	graph = build_graph(edges)
	return has_path(graph, nodeA, nodeB, set())

def build_graph(edges: list) -> dict:
	graph = {}
	for edge in edges:
		[a, b] = edge
		if a not in graph:
			graph[a] = []
		if b not in graph:
			graph[b] = []
		graph[a].append(b)
		graph[b].append(a)
	return graph

def has_path(graph: dict, src: str, dst: str, visited: set) -> bool:
	if src is dst:
		return True
	if src in visited:
		return False

	visited.add(src)

	for neighbor in graph[src]:
		if has_path(graph, neighbor, dst, visited) is True:
			return True
	return False


edges = [
	['i', 'j'],
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
]

print(undirected_path(edges, 'j', 'm'))  # True

# Complexity
# n = number of nodes
# e = n ^ 2 = number of edges
# Time: O(e) = O(n ^ 2)
# Space: O(n) 