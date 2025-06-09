# LEETOCE 709

'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''

def toLowerCase(s):
    return s.lower()

# Example usage:
s = "Hello"
print(toLowerCase(s))  # Output: "hello"

s2 = "LeetCode"
print(toLowerCase(s2))  # Output: "leetcode"

s3 = "LOVELY"
print(toLowerCase(s3))  # Output: "lovely"

s4 = "Job"
print(toLowerCase(s4))  # Output: "job"

s5 = "Python3"
print(toLowerCase(s5))  # Output: "python3"