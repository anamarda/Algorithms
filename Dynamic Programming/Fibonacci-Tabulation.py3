# Write a function 'fib(n)' that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
#
# The qst and 2nd number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two. 
#
# eg: fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Use tabulation.
def fib(n: int) -> int:
	table = [0] * (n + 2)
	table[1] = 1
	for i in range(n):
		table[i + 1] += table[i]
		table[i + 2] += table[i]
	return table[n]

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025

# Complexity
# Time: O(n)
# Space: O(n)