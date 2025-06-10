# LEETCODE 2000

'''
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
'''

def reversePrefix(word, ch):
    index = word.find(ch)
    if index == -1:
        return word
    return word[:index + 1] [::-1] + word[index + 1:]

# Example usage:
word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))  # Output: "dcbaefd"

# Another example:
word = "xyxz"
ch = "z"
print(reversePrefix(word, ch))  # Output: "zyxx"

# Yet another example:
word = "hello"
ch = "x"
print(reversePrefix(word, ch))  # Output: "hello" (ch not found, so no change)

# Yet another example:
word = "abcde"
ch = "a"
print(reversePrefix(word, ch))  # Output: "abcde" (ch is the first character, so no change)

# Yet another example:
word = "abcdefg"
ch = "g"
print(reversePrefix(word, ch))  # Output: "gfedcba" (ch is the last character, so the entire string is reversed)