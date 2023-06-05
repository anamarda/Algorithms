# Write a function countConstruct(target, wordBank) that accepts a
# target string and an array of strings.
#
# The function should return the number of ways that the target can
# be constructed by concatenating elements of the wordBank array.
#
# You may reuse elements of wordBank as many times as needed.

# Use tabulation.
def countConstruct(targetSum: str, wordBank: list) -> int:
	table = [0] * (len(targetSum) + 1)
	table[0] = 1
	for i in range(len(targetSum)):
		if table[i] == 0:
			continue
		for word in wordBank:
			if targetSum[i : i + len(word)] == word:
				table[i + len(word)] += table[i]
	return table[len(targetSum)]

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0

# Complexity
# m = target, n = len(wordBank)
# Time: O(m*n*m)
# Space: O(m)