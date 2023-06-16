# Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water 
# and L represents land. The function should return the size of the smallest island. An island is a 
# vertically or horizontally connected region of land.
#
# You may assume that the grid contains at least one island.


def minimum_island(grid) -> int:
	visited = set()
	minimum = float('inf')
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			island_size = explore_size(grid, r, c, visited)
			if island_size > 0 and island_size < minimum:
				minimum = island_size

	return minimum

def explore_size(grid, r, c, visited) -> int:
	rowInBounds = r >= 0 and r < len(grid)
	columnInBounds = c >= 0 and c < len(grid[0])
	if not rowInBounds or not columnInBounds:
		return 0

	if grid[r][c] == 'W':
		return 0

	pos = str(r) + ',' + str(c)
	if pos in visited:
		return 0
	visited.add(pos)

	size = 1
	size += explore_size(grid, r - 1, c, visited)
	size += explore_size(grid, r + 1, c, visited)
	size += explore_size(grid, r, c - 1, visited)
	size += explore_size(grid, r, c + 1, visited)

	return size


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid))  # -> 2

# Complexity
# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)