# LEETCODE 2185

'''
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.
'''

def prefixCount(words, pref):
    count = 0
    for word in words:
        count += word.startswith(pref)
    return count 

# Example usage:
words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(prefixCount(words, pref))  # Output: 2

words2 = ["leetcode", "win", "loops", "success"]
pref2 = "code"
print(prefixCount(words2, pref2))  # Output: 0

words3 = ["apple", "banana", "cherry", "date"]
pref3 = "a"
print(prefixCount(words3, pref3))  # Output: 1

words4 = ["hello", "world", "hell", "heaven"]
pref4 = "he"
print(prefixCount(words4, pref4))  # Output: 3