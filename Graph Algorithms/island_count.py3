# Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and 
# L represents land. The function should return the number of islands on the grid. An island is a 
# vertically or horizontally connected region of land.


def island_count(grid) -> int:
  visited = set()
  count = 0

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c, visited) == True:
        count += 1

  return count  

def explore(grid, r, c, visited):
  rowInBounds = r >= 0 and r < len(grid)
  columnInBounds = c >= 0 and c < len(grid[0])
  if not rowInBounds or not columnInBounds:
    return False

  pos = str(r) + ',' + str(c)
  if pos in visited:
    return False
  visited.add(pos)

  if grid[r][c] == 'W':
    return False

  explore(grid, r - 1, c, visited)
  explore(grid, r + 1, c, visited)
  explore(grid, r, c - 1, visited)
  explore(grid, r, c + 1, visited)

  return True


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))  # -> 3


# Complexity
# r = number of rows
# c = number of columns
# Time: O(rc)
# Space: O(rc)