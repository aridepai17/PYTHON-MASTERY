# LEETCODE 58

# Given a string s consisting of words and spaces, return the length of the last word in the string.

def lengthoflastword(s):
    words = s.strip().split()
    return len(words[-1]) if words else 0

# Example usage:
s = "Hello World"
print(lengthoflastword(s))  # Output: 5

# Another example usage:
s = "   fly me   to   the moon  "
print(lengthoflastword(s))  # Output: 4

# Yet another example usage:
s = "luffy is still joyboy"
print(lengthoflastword(s))  # Output: 6







