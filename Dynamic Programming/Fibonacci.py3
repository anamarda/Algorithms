# Write a function 'fib(n)' that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
#
# The qst and 2nd number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two. 
#
# eg: fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The straight forward, classic implementation.
# Recursive.
def fibRecursive(n: int) -> int:
	if n <= 2:
		return 1
	return fibRecursive(n - 1) + fibRecursive(n - 2)

print(fibRecursive(6)) # 8
print(fibRecursive(7)) # 13
print(fibRecursive(8)) # 21
#print(fibRecursive(50)) # 12586269025
# The last call takes too much time.

# Apply memoization.
def fibMemoization(n: int, memo: dict = {}) -> int:
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1
	memo[n] = fibMemoization(n - 1, memo) + fibMemoization(n - 2, memo)
	return memo[n]

print(fibMemoization(6)) # 8
print(fibMemoization(7)) # 13
print(fibMemoization(8)) # 21
print(fibMemoization(50)) # 12586269025