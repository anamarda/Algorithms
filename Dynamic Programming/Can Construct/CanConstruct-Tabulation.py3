# Write a function canConstruct(target, wordBank) that accepts a
# target string and an array of strings.
#
# The function should return a boolean indicating whether or not the
# targe can be constructed by concatenating elements of the
# wordBank array.
#
# You may reuse elements of wordBank as many times as needed.

# Use tabulation.
def canConstruct(targetSum: str, wordBank: list) -> bool:
	table = [False] * (len(targetSum) + 1)
	table[0] = True

	for i in range(len(targetSum)):
		if table[i] == False:
			continue
		for word in wordBank:
			# if the word matches the characters starting at position i
			if targetSum[i : i + len(word)] == word:
				table[i + len(word)] = True
	return table[len(targetSum)]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false

# Complexity
# m = target, n = len(wordBank)
# Time: O(m*n*m)
# Space: O(m)