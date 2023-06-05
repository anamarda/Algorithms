# Write a function 'fib(n)' that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
#
# The 1st and 2nd number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two. 
#
# eg: fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Apply memoization.
def fib(n: int, memo: dict = {}) -> int:
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1
	memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
	return memo[n]

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025

# Complexity
# Time: O(n)
# Space: O(n)