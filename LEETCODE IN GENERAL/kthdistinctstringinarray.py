# LEETCODE 2053

'''
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
'''

def kthDistinct(arr, k):
    frequency = {}
    
    for word in arr:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    distinctcount = 0
    for word in arr:
        if frequency[word] == 1:
            distinctcount += 1
            if distinctcount == k:
                return word
    return ""

# Example usage
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
result = kthDistinct(arr, k)
print(result)  # Output: "a"

# Another example usage
arr = ["aaa", "aa", "a", "b"]
k = 1
result = kthDistinct(arr, k)
print(result)  # Output: "b"

# Yet another example usage
arr = ["a", "b", "a"]
k = 3
result = kthDistinct(arr, k)
print(result)  # Output: ""