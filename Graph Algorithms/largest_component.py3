# Write a function, largestComponent, that takes in the adjacency list of an undirected graph. 
# The function should return the size of the largest connected component in the graph.


def largest_component(graph: dict) -> int:
	connected_component_size = 0
	visited = set()

	for node in graph:
		current_size = explore(graph, node, visited)
		if current_size > connected_component_size:
			connected_component_size = current_size

	return connected_component_size

def explore(graph: dict, current: int, visited: set) -> int:
	if current in visited:
		return 0

	visited.add(current)

	size = 1  # the current node

	for neighbor in graph[current]:
		size = size + explore(graph, neighbor, visited)

	return size

print(largest_component({
  '0': ['8', '1', '5'],
  '1': ['0'],
  '5': ['0', '8'],
  '8': ['0', '5'],
  '2': ['3', '4'],
  '3': ['2', '4'],
  '4': ['3', '2']
}))  # -> 4


# Complexity
# n = number of nodes
# e = n ^ 2 = number of edges
# Time: O(e) = O(n ^ 2)
# Space: O(n)