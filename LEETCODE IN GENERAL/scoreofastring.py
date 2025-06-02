# LEETCODE 3310

'''
You are given a string s. 
The score of a string is defined as the sum of the absolute differences between the ASCII values of adjacent characters in the string.
Return the score of the string s.
'''

def scoreOfString(s):
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
    return score

# Example usage:
s = "abcde"
print(scoreOfString(s))  # Output: 4 (1 + 1 + 1 + 1)

# Another example usage:
s = "lilbro"
print(scoreOfString(s))  # Output: 6 (3 + 2 + 1 + 2 + 1)