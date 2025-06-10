# LEETCODE 1662

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

def arrayStringsAreEqual(word1, word2):
    return ''.join(word1) == ''.join(word2)

# Example usage:
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))  # Output: True

word3 = ["a", "b", "c"]
word4 = ["ab", "c"]
print(arrayStringsAreEqual(word3, word4))  # Output: True

word5 = ["hello", "world"]
word6 = ["helloworld"]
print(arrayStringsAreEqual(word5, word6))  # Output: True

word7 = ["abc", "def"]
word8 = ["abcd", "ef"]
print(arrayStringsAreEqual(word7, word8))  # Output: True

word9 = ["", "abc"]
word10 = ["abc"]
print(arrayStringsAreEqual(word9, word10))  # Output: True

word11 = ["a", "b", "c"]
word12 = ["a", "cb"]
print(arrayStringsAreEqual(word11, word12))  # Output: False