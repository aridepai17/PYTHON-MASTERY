# LEETCODE 1446

'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.
'''

def maxPower(s):
    maximumPower = 1
    currentPower = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            currentPower += 1
            maximumPower = max(maximumPower, currentPower)
        else:
            currentPower = 1
    return maximumPower

# Example usage
s1 = "leetcode"
print(maxPower(s1))  # Output: 2

s2 = "abbcccddddeeeeedcba"
print(maxPower(s2))  # Output: 5

s3 = "triplepillooooow"
print(maxPower(s3))  # Output: 5

s4 = "hooraaaaaaaaaaay"
print(maxPower(s4))  # Output: 11

s5 = "tourist"
print(maxPower(s5))  # Output: 1

s6 = "a"
print(maxPower(s6))  # Output: 1

s7 = "bbbbb"
print(maxPower(s7))  # Output: 5

s8 = "abcde"
print(maxPower(s8))  # Output: 1

s9 = "aaabbbcccddd"
print(maxPower(s9))  # Output: 3

s10 = "aabbbbbcc"
print(maxPower(s10))  # Output: 5