# Say that you are a traveler on a 2D grid. You begin in the
# top-left corner and your goal is to travel to the bottom-righ
# corner. You may only move DOWN or RIGHT.
#
# In how many ways can you travel to the goal on a grid with
# dimensions m * n?
#
# Write a function gridTraveler(m, n) that calculates this.

# Tabulation.
def gridTraveler(m: int, n: int) -> int:
	table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	table[1][1] = 1

	for i in range(m + 1):
		for j in range(n + 1):
			current = table[i][j]
			if j + 1 <= n:
				table[i][j + 1] = table[i][j + 1] + current
			if i + 1 <= m:
				table[i + 1][j] = table[i + 1][j] + current

	return table[m][n]

print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6
print(gridTraveler(18, 18)) # 2333606220

# Complexity
# Time: O(m * n)
# Space: O(m * n)