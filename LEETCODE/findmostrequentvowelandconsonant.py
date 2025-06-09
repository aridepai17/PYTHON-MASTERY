# LEETCODE 3541

'''
You are given a string s consisting of lowercase English letters ('a' to 'z').
Your task is to:
1. Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
2. Find the consonant (all other letters excluding vowels) with the maximum frequency.
3. Return the sum of the two frequencies.

Note:
If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. 
If there are no vowels or no consonants in the string, consider their frequency as 0.
The frequency of a letter x is the number of times it occurs in the string.
'''

from collections import Counter

def maxFreqSum(s):
    vowels = set('aeiou')
    frequency = Counter(s)
    
    maxvowelfrequency = 0
    maxconsonantfrequency = 0
    
    for char, count in frequency.items():
        if char in vowels:
            maxvowelfrequency = max(maxvowelfrequency, count)
        else:
            maxconsonantfrequency = max(maxconsonantfrequency, count)
            
    return maxvowelfrequency + maxconsonantfrequency

# Example usage:
s = "hello"
print(maxFreqSum(s))  # Output: 3

s2 = "leetcode"
print(maxFreqSum(s2))  # Output: 4

s3 = "aabbcc"
print(maxFreqSum(s3))  # Output: 4

s4 = "xyz"
print(maxFreqSum(s4))  # Output: 1

s5 = "successes"
print(maxFreqSum(s5))  # Output: 6

s6 = "aeiaeia"
print(maxFreqSum(s6))  # Output: 3