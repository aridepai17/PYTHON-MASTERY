# LEETCODE 344

'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
'''

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
# Example usage:
s = ["h", "e", "l", "l", "o"]
reverseString(s)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
reverseString(s2)  # Output: ["h", "a", "n", "n", "a", "H"]

s3 = ["a", "b", "c", "d"]
reverseString(s3)  # Output: ["d", "c", "b", "a"]

s4 = ["r", "e", "v", "e", "r", "s", "e"]
reverseString(s4)  # Output: ["e", "s", "r", "e", "v", "e", "r"]

s5 = ["P", "y", "t", "h", "o", "n"]
reverseString(s5)  # Output: ["n", "o", "h", "t", "y", "P"]

s6 = ["L", "e", "e", "t", "C", "o", "d", "e"]
reverseString(s6)  # Output: ["e", "d", "o", "C", "t", "e", "e", "L"]