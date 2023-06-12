# Write a function, shortestPath, that takes in an array of edges for an undirected graph and two 
# nodes (nodeA, nodeB). The function should return the length of the shortest path between A 
# and B. Consider the length as the number of edges in the path, not the number of nodes. If 
# there is no path between A and B, then return -1.


def shortest_path(edges: list, nodeA: str, nodeB: str) -> int:
	graph = build_graph(edges)
	visited = set()
	count = bfs(graph, nodeA, nodeB)
	return count

def bfs(graph: dict, src: str, dst: str) -> int:
	queue = [ [src, 0] ]
	visited = set()
	visited.add(src)

	while len(queue) > 0:
		[current, distance] = queue.pop(0)
		
		if current == dst:
				return distance

		for neighbor in graph[current]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append([neighbor, distance + 1])

	return -1

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


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))  # -> 2 

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
];

print(shortest_path(edges, 'b', 'g'))  # -> -1