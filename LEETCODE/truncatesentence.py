# LEETCODE 1816

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).
You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words.
Return s after truncating it.
'''

def truncateSentence(s, k):
    words = s.split()
    return ' '.join(words[:k])

# Example usage:
s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))  # Output: "Hello how are you"

# Example usage with fewer words than k
s = "Hello"
k = 10
print(truncateSentence(s, k))  # Output: "Hello"

# Example usage with exactly k words
s = "This is a test sentence"
k = 5
print(truncateSentence(s, k))  # Output: "This is a test sentence"

# Yet another example with punctuation
s = "Truncate this sentence please!"
k = 3
print(truncateSentence(s, k))  # Output: "Truncate this sentence"