#LEETCODE 1455

'''
Given a sentence that consists of some words separated by a single space, 
and a searchWord, check if searchWord is a prefix of any word in sentence.
Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
If there is no such word return -1.
A prefix of a string is any leading contiguous substring of that string.
'''

def isPrefixOfWord(sentence, searchWord):
  words = sentence.split()
    
  for index, word in enumerate(words):
    if word.startswith(searchWord):
        return index + 1
  return -1

# Example usage
sentence1 = "i love eating burger"
searchWord1 = "burg"
print(isPrefixOfWord(sentence1, searchWord1))  # Output: 3

# Additional examples
sentence2 = "this problem is easy"
searchWord2 = "pro"
print(isPrefixOfWord(sentence2, searchWord2))  # Output: 2

sentence3 = "hello world"
searchWord3 = "wor"
print(isPrefixOfWord(sentence3, searchWord3))  # Output: 2

sentence4 = "apple banana cherry"
searchWord4 = "che"
print(isPrefixOfWord(sentence4, searchWord4))  # Output: 3

sentence5 = "python java cplusplus"
searchWord5 = "jav"
print(isPrefixOfWord(sentence5, searchWord5))  # Output: 2

sentence6 = "find the prefix in this sentence"
searchWord6 = "pre"
print(isPrefixOfWord(sentence6, searchWord6))  # Output: 3

sentence7 = "no match here"
searchWord7 = "xyz"
print(isPrefixOfWord(sentence7, searchWord7))  # Output: -1

sentence8 = "prefix prefix prefix"
searchWord8 = "pre"
print(isPrefixOfWord(sentence8, searchWord8))  # Output: 1

sentence9 = "a ab abc abcd"
searchWord9 = "abc"
print(isPrefixOfWord(sentence9, searchWord9))  # Output: 3

sentence10 = "look for the first occurrence"
searchWord10 = "for"
print(isPrefixOfWord(sentence10, searchWord10))  # Output: 2