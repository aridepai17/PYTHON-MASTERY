# LEETCODE 2769

'''
Given two integers, num and t. 
A number x is achievable if it can become equal to num after applying the following operation at most t times:
- Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible value of x.
'''

def findMaximumAchievableNumber(num, t):
    return num + t * 2

# Explanation how the answer becomes num + t * 2:
# - If we increase x by 1, we can also increase num by 1.
# - If we decrease x by 1, we can also decrease num by 1.
# - Each operation allows us to adjust both x and num by 1.
# - Therefore, after t operations, we can adjust x by t and num by t.

# Example usage:
num = 5
t = 3
print(findMaximumAchievableNumber(num, t))  # Output: 11

# Another example:
num = 10
t = 2
print(findMaximumAchievableNumber(num, t))  # Output: 14

# Yet another example:
num = 0
t = 5
print(findMaximumAchievableNumber(num, t))  # Output: 10

# More examples:
num = -3
t = 4
print(findMaximumAchievableNumber(num, t))  # Output: 1