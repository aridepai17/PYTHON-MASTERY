# LEETCODE 1957

'''
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.
'''

def makeFancyString(s):
    result = []
    for char in s:
        if len(result) >= 2 and result[-1] == result[-2] == char:
            continue
        result.append(char)
    return ''.join(result)

# Example usage:
s = "leeetcode"
print(makeFancyString(s))  # Output: "leetcode"

# Additional examples:
s = "aaabaaaa"
print(makeFancyString(s))  # Output: "aabaa"

s = "aab"
print(makeFancyString(s))  # Output: "aab"

s = "aa"
print(makeFancyString(s))  # Output: "aa"

s = "abc"
print(makeFancyString(s))  # Output: "abc"

s = "aabbcc"
print(makeFancyString(s))  # Output: "aabbcc"

s = "aaaabbbbcccc"
print(makeFancyString(s))  # Output: "aabbcc"

s = "xxxyyyzzz"
print(makeFancyString(s))  # Output: "xxyyzz"

s = "noon"
print(makeFancyString(s))  # Output: "noon"