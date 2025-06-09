# LEETCODE 2124

'''
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. 
Otherwise, return false.
'''

def checkString(s):
    return 'ba' not in s

# Alternate solution 

def checkString(s):
    foundb = False
    for char in s:
        if char == 'b':
            foundb = True
        elif char == 'a' and foundb:
            return False
    return True

# Example usage:
s1 = "aaabbb"
print(checkString(s1))  # Output: True

s2 = "abab"
print(checkString(s2))  # Output: False

s3 = "aabbb"
print(checkString(s3))  # Output: True

s4 = "bbaaa"
print(checkString(s4))  # Output: False