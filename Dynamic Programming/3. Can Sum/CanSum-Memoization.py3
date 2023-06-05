# Write a function canSum(targetSum, numbers) that takes in a
# targetSum and an array of numbers as arguments.
#
# The function should return a boolean indicating whether or not it
# is possible to generate the targetSum using numbers from the array.
#
# You may use an element of the array as many times as needed.
# 
# You may assume that all input numbers are nonnegative.

# Apply memoization.
def canSum(targetSum: int, numbers: list, memo: dict) -> bool:
	if targetSum in memo:
		return memo[targetSum]
	if targetSum == 0:
		return True
	if targetSum < 0:
		return False

	for num in numbers:
		remainder = targetSum - num
		if canSum(remainder, numbers, memo) == True:
			memo[targetSum] = True
			return True

	memo[targetSum] = False
	return False

print(canSum(7, [2, 3], {})) # true
print(canSum(7, [5, 3, 4, 7], {})) # true
print(canSum(7, [2, 4], {})) # false
print(canSum(8, [2, 3, 5], {})) # true
print(canSum(300, [7, 14], {})) # false

# Complexity
# m = target sum, n = len(numbers)
# Time: O(m * n)
# Space: O(m)