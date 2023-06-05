# Write a function allConstruct(target, wordBank) that accepts a
# target string and an array of strings.
#
# The function should return a 2D array containing all the ways 
# that the target can be constructed by concatenating elements of
# the wordBank array. Each element of the 2D array should represent
# one combination that constructs the target.
#
# You may reuse elements of wordBank as many times as needed.

# Use tabulation.
def allConstruct(targetSum: str, wordBank: list) -> list:
	table = [[]] * (len(targetSum) + 1)
	table[0] = [[]]
	for i in range(len(targetSum)):
		for word in wordBank:
			if targetSum[i : i + len(word)] == word:
				newCombinations = map(lambda l: l + [word], table[i])
				table[i + len(word)] = table[i + len(word)] + list(newCombinations)
	return table[len(targetSum)]

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#	['purp', 'le'], 
#	['p', 'ur', 'p', 'le']
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])) 
# [
#	['abc', 'def'], 
#	['ab', 'c', 'def'], 
#	['abcd', 'ef'], 
#	['ab', 'cd', 'ef']
#]

print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# []

print(allConstruct("eeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
# []

# Complexity
# m = len(target), n = len(wordBank)
# Time: O(n^m) # We can't do any better because we need ALL the combinations.
# Space: O(n^m)