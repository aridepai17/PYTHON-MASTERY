# LEETCODE 1684

'''
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''

def countConsistentStrings(allowed, words):
    allowedset = set(allowed)
    count = 0
    
    for word in words:
        isconsistent = True
        for char in word:
            if char not in allowedset:
                isconsistent = False
                break
        if isconsistent:
            count += 1
    return count 

# Example usage:
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))  # Output: 2

# Another example usage:
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed, words))  # Output: 7

# Yet another example usage:
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed, words))  # Output: 4