# LEETCODE 884

'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
'''
from collections import Counter

def uncommonFromSentences(s1, s2):
    count1 = Counter(s1.split())
    count2 = Counter(s2.split())
    
    totalCount = count1 + count2
    
    return [ word for word in totalCount if totalCount[word] == 1 ] 

# Example usage:
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))  # Output: ['sweet', 'sour']

# Additional examples:
s1 = "apple banana orange"
s2 = "banana grape apple"
print(uncommonFromSentences(s1, s2))  # Output: ['orange', 'grape']

s1 = "hello world"
s2 = "hello there"
print(uncommonFromSentences(s1, s2))  # Output: ['world', 'there']

s1 = "a b c d"
s2 = "e f g h"
print(uncommonFromSentences(s1, s2))  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    