# LEETCODE 2788

'''
Given an array of strings words and a character separator, split each string in words by separator.
Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes
- separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
- A split may result in more than two strings.
- The resulting strings must maintain the same order as they were initially given.
'''

def splitWordsBySeparator(words, separator):
    result = []
    for word in words:
        for w in word.split(separator):
            if w:
                result.append(w)
    return result

# Time Complexity: O(n * m), where n is the number of words and m is the average length of each word.
# Space Complexity: O(k), where k is the total number of non-empty strings after splitting.

# Alternate solution
def splitWordsBySeparatorAlt(words, separator):
    return [w for word in words for w in word.split(separator) if w]

# Example usage:
words = ["one.two.three", "four.five", "six"]
separator = "."
print(splitWordsBySeparator(words, separator))  # Output: ['one', 'two', 'three', 'four', 'five', 'six']

# Additional examples:
words = ["apple,banana,orange", "grape,kiwi"]
separator = ","
print(splitWordsBySeparator(words, separator))  # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi']

words = ["hello|world", "python|is|great"]
separator = "|"
print(splitWordsBySeparator(words, separator))  # Output: ['hello', 'world', 'python', 'is', 'great']

words = ["a.b.c.d", "e.f.g.h"]
separator = "."
print(splitWordsBySeparator(words, separator))  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

words = ["no-separator-here"]
separator = "-"
print(splitWordsBySeparator(words, separator))  # Output: ['no', 'separator', 'here']

words = ["", "empty", "", "strings"]
separator = "|"
print(splitWordsBySeparator(words, separator))  # Output: ['empty', 'strings']

words = ["one..two...three", "four....five"]
separator = "."
print(splitWordsBySeparator(words, separator))  # Output: ['one', 'two', 'three', 'four', 'five']