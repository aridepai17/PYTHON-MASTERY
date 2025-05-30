# LEETCODE 9

# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x):
    return str(x) == str(x)[::-1]


# Example usage:
x = 121
print(isPalindrome(x))  # Output: True

x = -121
print(isPalindrome(x))  # Output: False

x = 10
print(isPalindrome(x))  # Output: False

x = 12321
print(isPalindrome(x))  # Output: True