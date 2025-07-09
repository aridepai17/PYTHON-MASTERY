# LEETCODE 2828

'''
Given an array of strings words and a string s, determine if s is an acronym of words.
The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order.
For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].
Return true if s is an acronym of words, and false otherwise.
'''

def isAcronym(words, s):
  acronym = ''.join(word[0] for word in words)
  return s == acronym

# Example usage:
words1 = ["apple", "banana", "cherry"]
s1 = "abc"
print(isAcronym(words1, s1))  # Output: True

words2 = ["dog", "cat", "fish"]
s2 = "dcf"
print(isAcronym(words2, s2))  # Output: True

words3 = ["hello", "world"]
s3 = "hw"
print(isAcronym(words3, s3))  # Output: True

words4 = ["python", "rocks"]
s4 = "pr"
print(isAcronym(words4, s4))  # Output: True

words5 = ["a", "b", "c"]
s5 = "abc"
print(isAcronym(words5, s5))  # Output: True

words6 = ["bear", "cat"]
s6 = "bc"
print(isAcronym(words6, s6))  # Output: True

words7 = ["apple", "banana"]
s7 = "ab"
print(isAcronym(words7, s7))  # Output: True

words8 = ["one", "two", "three"]
s8 = "ot"
print(isAcronym(words8, s8))  # Output: False

words9 = ["red", "blue", "green"]
s9 = "rgb"
print(isAcronym(words9, s9))  # Output: True

words10 = ["sun", "moon"]
s10 = "sm"
print(isAcronym(words10, s10))  # Output: True