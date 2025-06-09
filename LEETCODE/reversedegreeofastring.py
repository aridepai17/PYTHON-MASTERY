# LEETCODE 3498

'''
Given a string s, calculate its reverse degree.
The reverse degree is calculated as follows:
1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
2. Sum these products for all characters in the string.
Return the reverse degree of s.
'''

def reverseDegree(s):
    degree = 0
    for index, value in enumerate(s):
        reversevalue = 26 - (ord(value) - ord('a'))
        degree += reversevalue * (index + 1)
    return degree

# Example usage:
s = "abc"
print(reverseDegree(s))  # Output: 148

# Another example:
s = "zaza"
print(reverseDegree(s))  # Output: 160

s = "xyz"
print(reverseDegree(s))  # Output: 10