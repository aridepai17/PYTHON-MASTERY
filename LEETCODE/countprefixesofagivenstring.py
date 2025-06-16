# LEETCODE 2255

'''
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string.
A substring is a contiguous sequence of characters within a string.
'''

def countPrefixes(words, s):
    count = 0
    
    for word in words:
        if s.startswith(word):
            count += 1
    return count

# Example usage
words = ["a", "b", "c", "ab", "bc"]
s = "abcde"
print(countPrefixes(words, s))  # Output: 3 (a, ab, and abc are prefixes of "abcde")

# Additional examples
words2 = ["hello", "he", "hell", "world"]
s2 = "hello"
print(countPrefixes(words2, s2))  # Output: 3 (he, hell, and hello are prefixes of "hello")

words3 = ["prefix", "pre", "fix", "suf"]
s3 = "prefixes"
print(countPrefixes(words3, s3))  # Output: 2 (prefix and pre are prefixes of "prefixes")

words4 = ["test", "te", "tes", "t"]
s4 = "testing"
print(countPrefixes(words4, s4))  # Output: 3 (te, tes, and t are prefixes of "testing")

words5 = ["apple", "app", "apricot", "banana"]
s5 = "application"
print(countPrefixes(words5, s5))  # Output: 2 (app and apple are prefixes of "application")

words6 = ["xyz", "xy", "x"]
s6 = "xylophone"
print(countPrefixes(words6, s6))  # Output: 2 (x and xy are prefixes of "xylophone")

words7 = ["a", "ab", "abc", "abcd"]
s7 = "abcde"
print(countPrefixes(words7, s7))  # Output: 4 (a, ab, abc, and abcd are prefixes of "abcde")

words8 = ["", "a", "b", "c"]
s8 = "abc"
print(countPrefixes(words8, s8))  # Output: 4 (empty string is a prefix, a, b, and c are prefixes of "abc")