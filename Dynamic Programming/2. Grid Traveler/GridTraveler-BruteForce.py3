# Say that you are a traveler on a 2D grid. You begin in the
# top-left corner and your goal is to travel to the bottom-righ
# corner. You may only move DOWN or RIGHT.
#
# In how many ways can you travel to the goal on a grid with
# dimensions m * n?
#
# Write a function gridTraveler(m, n) that calculates this.

# Brute force.
def gridTraveler(m: int, n: int) -> int:
	if m == 1 and n == 1:
		return 1
	if m == 0 or n == 0:
		return 0
	return gridTraveler(m - 1, n) + gridTraveler (m, n - 1)

print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6
print(gridTraveler(18, 18)) # 2333606220
# The last call takes too much time.

# Complexity
# Time: O(2^(n + m))
# Space: O(m + n)