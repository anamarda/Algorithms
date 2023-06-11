# has path
# Write a function, has_path, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes
# (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and 
# destination nodes.

def has_path_dfs(graph: dict, src: str, dst: str) -> bool:
	if src == dst:
		return True
	for neighbor in graph[src]:
		if has_path_dfs(graph, neighbor, dst) is True:
			return True
	return False

def has_path_bfs(graph: dict, src: str, dst: str) -> bool:
	queue = [ src ]
	while len(queue) > 0:
		current = queue.pop(0)
		if current == dst:
			return True
		for neighbor in graph[current]:
			queue.append(neighbor)
	return False

graph = {
	'f': ['g', 'i'],
	'g': ['h'],
	'h': [],
	'i': ['g', 'k'],
	'j': ['i'],
	'k': []
}

print(has_path_dfs(graph, 'f', 'k'))  # True
print(has_path_bfs(graph, 'f', 'k'))  # True

# Complexity
# n = number of nodes
# e = n ^ 2 = number of edges
# Time: O(e) = O(n ^ 2)
# Space: O(n) 