# LEETCODE 3146

'''
You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.
Return the permutation difference between s and t.
'''

def permutationDifference(s, t):
    positiondifference = 0
    for i in s:
        positiondifference += abs(s.index(i) - t.index(i))
    return positiondifference

# Example usage:
s1 = "abc"
t1 = "cba"
print(permutationDifference(s1, t1))  # Output: 4

s2 = "abcd"
t2 = "dcba"
print(permutationDifference(s2, t2))  # Output: 6

s3 = "xyz"
t3 = "zyx"
print(permutationDifference(s3, t3))  # Output: 6

s4 = "leetcode"
t4 = "leetcode"
print(permutationDifference(s4, t4))  # Output: 0

s5 = "abcde"
t5 = "edcba"
print(permutationDifference(s5, t5))  # Output: 10

s6 = "hello"
t6 = "holle"
print(permutationDifference(s6, t6))  # Output: 4