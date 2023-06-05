# Write a function 'fib(n)' that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
#
# The 1st and 2nd number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two. 
#
# eg: fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Brute force.
def fib(n: int) -> int:
	if n <= 2:
		return 1
	return fib(n - 1) + fib(n - 2)

print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025
# The last call takes too much time.

# Complexity
# Time: O(2^n) ---> exponential (this can be optimized)
# Space: O(n)