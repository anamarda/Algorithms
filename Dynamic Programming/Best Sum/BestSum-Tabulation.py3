# Write a function bestSum(targetSum, numbers) that takes in a
# targetSum and an array of numbers as arguments.
#
# The function should return an array containing the shortest
# combination of numbers that add up to exactly the targetSum.
#
# If there is a tie for the shortest combination, you may return any 
# one of the shortest.

# Use tabulation.
def bestSum(targetSum: int, numbers: list) -> list:
	table = [None] * (targetSum + 1)
	table[0] = []
	for i in range(targetSum):
		if table[i] == None:
			continue
		for num in numbers:
			idx = i + num
			if idx > targetSum:
				continue
			combination = table[i] + [num]
			if table[idx] == None or len(combination) < len(table[idx]): 
				table[idx] = combination

	return table[targetSum]

print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
print(bestSum(100, [25, 5, 1, 2])) # [25, 25, 25, 25]
print(bestSum(300, [7, 14])) # null

# Complexity
# Time: O(m*n*m)
# Space: O(m^2)