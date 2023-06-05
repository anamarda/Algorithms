# Write a function howSum(targetSum, numbers) that takes in a
# targetSum and an array of numbers as arguments.
#
# The function should return an array containing any combination of
# elements that add up to exactly the targetSum.
#
# If there is no combination that adds up to the targetSum, then 
# return null.
# 
# If there are multiple combinations possible, you may return any
# single one.

# Use tabulation.
def howSum(targetSum: int, numbers: list) -> list:
	table = [None] * (targetSum + 1)
	table[0] = []
	for i in range(targetSum):
		if table[i] == None:
			continue
		for num in numbers:
			idx = i + num
			if idx > targetSum:
				continue
			table[i + num] = table[i] + [num]

	return table[targetSum]

print(howSum(7, [2, 3])) # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # [4, 3]
print(howSum(7, [2, 4])) # null
print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2]
print(howSum(300, [7, 14])) # null

# Complexity
# Time: O(m*n*m)
# Space: O(m^2)