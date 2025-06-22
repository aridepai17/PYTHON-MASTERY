# LEETCODE 383

'''
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''
from collections import Counter

def canConstruct(ransomNote, magazine):
    ransomCount = Counter(ransomNote)
    magazineCount = Counter(magazine)
    
    for char in ransomCount:
        if ransomCount[char] > magazineCount[char]:
            return False
    return True

# Alternate solution ( one-pass )
def canConstructOnePass(ransomNote, magazine):
    return Counter(ransomNote) <= Counter(magazine)

# Example usage
ransomNote1 = "a"
magazine1 = "b"
print(canConstruct(ransomNote1, magazine1))  # Output: False

ransomNote2 = "aa"
magazine2 = "aab"
print(canConstruct(ransomNote2, magazine2))  # Output: True

ransomNote3 = "aa"
magazine3 = "ab"
print(canConstruct(ransomNote3, magazine3))  # Output: False

ransomNote4 = "abc"
magazine4 = "aabbcc"
print(canConstruct(ransomNote4, magazine4))  # Output: True

ransomNote5 = "aabbc"
magazine5 = "aabbcc"
print(canConstruct(ransomNote5, magazine5))  # Output: True

ransomNote6 = "aabbcc"
magazine6 = "abc"
print(canConstruct(ransomNote6, magazine6))  # Output: False

ransomNote7 = ""
magazine7 = "anything"
print(canConstruct(ransomNote7, magazine7))  # Output: True

ransomNote8 = "abc"
magazine8 = ""
print(canConstruct(ransomNote8, magazine8))  # Output: False

ransomNote9 = "aabb"
magazine9 = "bbaa"
print(canConstruct(ransomNote9, magazine9))  # Output: True

ransomNote10 = "xyz"
magazine10 = "xyyzz"
print(canConstruct(ransomNote10, magazine10))  # Output: False