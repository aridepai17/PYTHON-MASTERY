# LEETCODE 520 

'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''

def detectCapitalUse(word):
  return word.isupper() or word.islower() or word.istitle()

# Example usage:
word1 = "USA"
print(detectCapitalUse(word1)) # True

# Additional examples:
word2 = "leetcode"
print(detectCapitalUse(word2)) # True

word3 = "Google"
print(detectCapitalUse(word3)) # True

word4 = "FlaG"
print(detectCapitalUse(word4)) # False

word5 = "HELLO"
print(detectCapitalUse(word5)) # True

word6 = "world"
print(detectCapitalUse(word6)) # True

word7 = "Python"
print(detectCapitalUse(word7)) # True

word8 = "cOdE"
print(detectCapitalUse(word8)) # False

word9 = "JAVA"
print(detectCapitalUse(word9)) # True

word10 = "tEst"
print(detectCapitalUse(word10)) # False