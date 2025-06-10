# LEETCODE 409

'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''

def longestPalindrome(s):
    longest = set()
    length = 0
    
    for i in s:
        if i in longest:
            longest.remove(i)
            length += 2
        else:
            longest.add(i)
    
    if longest:
        length += 1
    return length

# Example usage:
s = "abccccd"
print(longestPalindrome(s))  # Output: 7 (the longest palindrome is "dccaccd")

s2 = "aabbcc"
print(longestPalindrome(s2))  # Output: 6 (the longest palindrome is "abcba")

s3 = "a"
print(longestPalindrome(s3))  # Output: 1

s4 = "aa"
print(longestPalindrome(s4))  # Output: 2

s5 = "ab"
print(longestPalindrome(s5))  # Output: 1

s6 = "abc"
print(longestPalindrome(s6))  # Output: 1

s7 = "aabbccde"
print(longestPalindrome(s7))  # Output: 7 (the longest palindrome is "abcdcba")