# LEETCODE 2108

'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
'''

def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:  
            return word
    return "" 

# Example usage:
words = ["abc", "car", "ada", "racecar", "cool"]
print(firstPalindrome(words))  # Output: "ada"

# Additional examples
words2 = ["not", "a", "palindrome"]
print(firstPalindrome(words2))  # Output: "" (No palindromic strings)

words3 = ["level", "world", "noon", "python"]
print(firstPalindrome(words3))  # Output: "level" (First palindromic string)

words4 = ["hello", "racecar", "madam"]
print(firstPalindrome(words4))  # Output: "racecar" (First palindromic string)

words5 = ["12321", "45654", "789"]
print(firstPalindrome(words5))  # Output: "12321" (First palindromic string)

words6 = ["", "a", "b"]
print(firstPalindrome(words6))  # Output: "" (Empty string is considered palindromic but not the first)

words7 = ["abc", "def", "ghi"]
print(firstPalindrome(words7))  # Output: "" (No palindromic strings)
    