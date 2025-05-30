# LEETCODE 2351

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

def repeatedCharacter(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
        
# Example usage:
s = "abccbaacz"
result = repeatedCharacter(s)
print(result)  # Output: "c"

# Another example usage:
s2 = "abcdd"
result2 = repeatedCharacter(s2)
print(result2)  # Output: "d"

s3 = "ajfajfaffajf"
result3 = repeatedCharacter(s3)
print(result3)  # Output: "a"

