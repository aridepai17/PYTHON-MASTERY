# LEETCODE 1941

'''
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''
from collections import Counter

def areOccurencesEqual(s):
  freq = {}
  
  for char in s:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  
  frequencyValues = set(freq.values())
  return len(frequencyValues) == 1


# Alternate solution using Counter()

def areOccurencesEqual(s):
  frequency = Counter(s)
  return len(set(frequency.values())) == 1

# Example usage
s = "abacbc"
print(areOccurencesEqual(s)) # True

s1 = "aabb"
print(areOccurencesEqual(s1)) # True

s2 = "abc"
print(areOccurencesEqual(s2)) # True

s3 = "aabbcc"
print(areOccurencesEqual(s3)) # True

s4 = "aaabbb"
print(areOccurencesEqual(s4)) # True

s5 = "abcabc"
print(areOccurencesEqual(s5)) # True

s6 = "a"
print(areOccurencesEqual(s6)) # True

s7 = ""
print(areOccurencesEqual(s7)) # True

s8 = "aabbc"
print(areOccurencesEqual(s8)) # False

s9 = "aabbccdd"
print(areOccurencesEqual(s9)) # True

s10 = "abcde"
print(areOccurencesEqual(s10)) # True
