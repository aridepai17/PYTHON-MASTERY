# LEETCODE 1832

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentenceSet = set(sentence)
    return alphabet.issubset(sentenceSet)

# Example usage:
sentence1 = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence1))  # Output: True

sentence2 = "leetcode"
print(checkIfPangram(sentence2))  # Output: False

sentence3 = "abcdefghijklmnopqrstuvwxyz"
print(checkIfPangram(sentence3))  # Output: True

sentence4 = "pack my box with five dozen liquor jugs"
print(checkIfPangram(sentence4))  # Output: True

sentence5 = "hello world"
print(checkIfPangram(sentence5))  # Output: False