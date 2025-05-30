# LEETCODE 125

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome(s):
    pal = [c.lower() for c in s if c.isalnum()]
    return pal == pal[::-1]

# Example usage:
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True

s = "race a car"
print(isPalindrome(s))  # Output: False

s = " "
print(isPalindrome(s))  # Output: True

s = "0P"
print(isPalindrome(s))  # Output: False

s = "A Toyota's a Toyota"
print(isPalindrome(s))  # Output: True