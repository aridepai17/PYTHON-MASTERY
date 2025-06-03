# LEETCODE 28

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
    
# Example usage:
needle = "ll"
haystack = "hello"
print(strStr(haystack, needle))  # Output: 2

# Another example usage:
needle = "bba"
haystack = "aaaaa"
print(strStr(haystack, needle))  # Output: -1
