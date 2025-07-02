# LEETCODE 500

'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
In the American keyboard:
- The first row consists of the characters "qwertyuiop",
- The second row consists of the characters "asdfghjkl", and
- The third row consists of the characters "zxcvbnm".
'''

def findWords(words):
  row1 = set("qwertyuiop")
  row2 = set("asdfghjkl")
  row3 = set("zxcvbnm")
  
  result = []
  for word in words:
    lower = set(word.lower())
    if lower <= row1 or lower <= row2 or lower <= row3:
      result.append(word)
  return result

# Example usage:
words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))  # Output: ['Alaska', 'Dad']

# Additional examples:
words1 = ["qwerty", "asdf", "zxcv", "hello"]
print(findWords(words1))  # Output: ['qwerty', 'asdf', 'zxcv']

words2 = ["Type", "writer", "keyboard", "row"]
print(findWords(words2))  # Output: ['Type', 'writer', 'row']

words3 = ["Alaska", "dad", "peace", "QWERTY"]
print(findWords(words3))  # Output: ['Alaska', 'dad', 'QWERTY']

words4 = ["abc", "def", "ghi"]
print(findWords(words4))  # Output: []

words5 = ["A", "S", "D", "F"]
print(findWords(words5))  # Output: ['A', 'S', 'D', 'F']

words6 = ["zxc", "vbn", "mnb"]
print(findWords(words6))  # Output: ['zxc', 'vbn', 'mnb']

words7 = ["HelloWorld", "Alaska", "Dad"]
print(findWords(words7))  # Output: ['Alaska', 'Dad']

words8 = ["qwe", "rty", "uio"]
print(findWords(words8))  # Output: ['qwe', 'rty', 'uio']

words9 = ["abcde", "fghij", "klmno"]
print(findWords(words9))  # Output: []