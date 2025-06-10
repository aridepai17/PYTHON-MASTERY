# LEETCODE 557

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s):
    words = s.split(' ')
    reversewords = [word[::-1] for word in words]
    return ' '.join(reversewords)

# Example usage:
s = "Let's take LeetCode contest"
print(reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"

# Another example:
s2 = "Hello World"
print(reverseWords(s2))  # Output: "olleH dlroW"

# Yet another example:
s3 = "a good   example"
print(reverseWords(s3))  # Output: "a doog   elpmaxe"

# Yet another example:
s4 = "  Leading and trailing spaces  "
print(reverseWords(s4))  # Output: "  gnidaeL dna gnilaert secaps  "

# Yet another example:
s5 = "SingleWord"
print(reverseWords(s5))  # Output: "drowelgniS" (single word, reversed)