# LEETCODE 2716

'''
Given a string s, you have two types of operation:
1. Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the left of i (if exists).
2. Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the right of i (if exists).
Your task is to minimize the length of s by performing the above operations zero or more times.
Return an integer denoting the length of the minimized string.
'''

def minimizeStringLength(s):
  return len(set(s))

# Example usage
s1 = "abcabc"
print(minimizeStringLength(s1))  # Output: 3

s2 = "aabbcc"
print(minimizeStringLength(s2))  # Output: 3

s3 = "abc"
print(minimizeStringLength(s3))  # Output: 3

s4 = "aaaa"
print(minimizeStringLength(s4))  # Output: 1

s5 = ""
print(minimizeStringLength(s5))  # Output: 0

s6 = "abcd"
print(minimizeStringLength(s6))  # Output: 4

s7 = "aabb"
print(minimizeStringLength(s7))  # Output: 2

s8 = "abcdeabcde"
print(minimizeStringLength(s8))  # Output: 5

s9 = "xyzxyzxyz"
print(minimizeStringLength(s9))  # Output: 3

s10 = "pqrpqrpqr"
print(minimizeStringLength(s10))  # Output: 3
