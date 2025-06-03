# LEETCODE 2942

'''
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order
'''

def findWordsContaining(words, x):
    return [ i for i, word in enumerate(words) if x in word ]

# Example usage:
words = ["hello", "world", "example", "character"]
x = 'e'
print(findWordsContaining(words, x)) # Output: [0, 2, 3]

# Another example usage:
words = ["apple", "banana", "cherry", "date"]
x = 'a'
print(findWordsContaining(words, x)) # Output: [0, 1, 3]