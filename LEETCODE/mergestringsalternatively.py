# LEETCODE 1768

'''
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''

def mergeAlternatively(word1, word2):
    result = ''
    length = max(len(word1), len(word2))
    
    for i in range(length):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    
    return result

# Example usage
word1 = "abc"
word2 = "pqr"
print(mergeAlternatively(word1, word2))  # Output: "apbqcr"

word3 = "ab"
word4 = "pqrs"
print(mergeAlternatively(word3, word4))  # Output: "apbqrs"

word5 = "abcd"
word6 = "pq"
print(mergeAlternatively(word5, word6))  # Output: "apbqcd"

word7 = "a"
word8 = "b"
print(mergeAlternatively(word7, word8))  # Output: "ab"

word9 = "abcde"
word10 = "xyz"
print(mergeAlternatively(word9, word10))  # Output: "axbyczde"

word11 = ""
word12 = "abc"
print(mergeAlternatively(word11, word12))  # Output: "abc"

word13 = "abc"
word14 = ""
print(mergeAlternatively(word13, word14))  # Output: "abc"

word15 = "wxyz"
word16 = "1234"
print(mergeAlternatively(word15, word16))  # Output: "w1x2y3z4"

word17 = "longerstring"
word18 = "short"
print(mergeAlternatively(word17, word18))  # Output: "lsohnogretrstring"