# LEETCODE 387

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

from collections import Counter

def firstUniqChar(s):
    unique = []
    
    for char in set(s):
        if s.count(char) == 1:
            unique.append(s.index(char))
    if unique == []:
        return -1
    else:
        return min(unique)
    
# Alternate solution
def firstUniqChar(s):
    frequency = Counter(s)
    
    for index, value in frequency.items():
        if value == 1:
            return s.index(index)
    return -1

# Another alternate solution
def firstUniqChar(s):
    frequency = Counter(s)
    
    for index, count in enumerate(s):
        if frequency[count] == 1:
            return index
    return -1
    
# Example usage:
s = "leetcode"
print(firstUniqChar(s))  # Output: 0 (the first unique character is 'l')

s2 = "loveleetcode"
print(firstUniqChar(s2))  # Output: 2 (the first unique character is 'v')

s3 = "aabb"
print(firstUniqChar(s3))  # Output: -1 (no unique characters)

s4 = "a"
print(firstUniqChar(s4))  # Output: 0 (the only character is unique)

s5 = "abaccdeff"
print(firstUniqChar(s5))  # Output: 1 (the first unique character is 'b')

s6 = "aabbccddeeffg"
print(firstUniqChar(s6))  # Output: 12 (the first unique character is 'g')