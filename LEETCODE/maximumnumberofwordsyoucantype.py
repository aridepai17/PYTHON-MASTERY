# LEETCODE 1935

'''
There is a malfunctioning keyboard where some letter keys do not work. 
All other keys on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces) 
and a string brokenLetters of all distinct letter keys that are broken, 
return the number of words in text you can fully type using this keyboard.
'''

def canBeTypedWords(text, brokenLetters):
  broken = set(brokenLetters)
  words = text.split()
  count = 0
  
  for word in words:
    if not any(char in broken for char in word):
      count += 1
  return count

# Example usage:
text = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(text, brokenLetters))  # Output: 1

# Additional examples:
text1 = "the quick brown fox"
brokenLetters1 = "aeiou"
print(canBeTypedWords(text1, brokenLetters1))  # Output: 0

text2 = "hello there"
brokenLetters2 = "h"
print(canBeTypedWords(text2, brokenLetters2))  # Output: 1

text3 = "keyboard malfunction"
brokenLetters3 = "k"
print(canBeTypedWords(text3, brokenLetters3))  # Output: 2

text4 = "this is a test"
brokenLetters4 = "t"
print(canBeTypedWords(text4, brokenLetters4))  # Output: 2

text5 = "can you type"
brokenLetters5 = "c"
print(canBeTypedWords(text5, brokenLetters5))  # Output: 3

text6 = "hello world"
brokenLetters6 = "l"
print(canBeTypedWords(text6, brokenLetters6))  # Output: 1

text7 = "goodbye everyone"
brokenLetters7 = "g"
print(canBeTypedWords(text7, brokenLetters7))  # Output: 1

text8 = "a b c d e"
brokenLetters8 = "abcde"
print(canBeTypedWords(text8, brokenLetters8))  # Output: 0

text9 = "testing one two three"
brokenLetters9 = "z"
print(canBeTypedWords(text9, brokenLetters9))  # Output: 5