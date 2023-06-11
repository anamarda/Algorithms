
def depth_first_search_iterative(graph: dict, source: str) -> None:
	stack = [ source ]
	while len(stack) > 0:
		current = stack.pop()
		print(current)
		for neighbour in graph[current]:
			stack.append(neighbour)

def depth_first_search_recursive(graph: dict, source: str) -> None:
	print(source)
	for neighbour in graph[source]:
		depth_first_search_recursive(graph, neighbour)

graph = {
	'a': ['c', 'b'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}

print('DFS iterative:')
depth_first_search_iterative(graph, 'a');  # abdfce
print('DFS recursive:')
depth_first_search_recursive(graph, 'a');  # abdfce