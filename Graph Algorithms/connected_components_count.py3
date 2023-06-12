# Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected 
# graph. The function should return the number of connected components within the graph.


def connected_components_count(graph: dict) -> int:
	visited = set()
	count = 0
	for node in graph:
		if explore(graph, node, visited) is True:
			count += 1
	return count

def explore(graph: dict, src: str, visited: set) -> bool:
	if src in visited:
		return False

	visited.add(src)

	for neighbor in graph[src]:
		explore(graph, neighbor, visited)

	return True

print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))  # -> 2


# Complexity
# n = number of nodes
# e = n ^ 2 = number of edges
# Time: O(e) = O(n ^ 2)
# Space: O(n) 