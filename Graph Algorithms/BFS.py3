def breadth_first_search_iterative(graph: dict, source: str) -> None:
	queue = [ source ]
	while len(queue) > 0:
		current = queue.pop(0)
		print(current)
		for neighbour in graph[current]:
			queue.append(neighbour)

graph = {
	'a': ['c', 'b'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}

print('BFS iterative:')
breadth_first_search_iterative(graph, 'a');  # acbedf