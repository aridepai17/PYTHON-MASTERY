# LEETCODE 3005 

'''
You are given an array nums such that those elements all have the maximum frequency.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in array
'''

from collections import Counter
def maxFrequencyElements(nums):
    frequency = Counter(nums)
    maxfreq = max(frequency.values())
    return sum(count for count in frequency.values() if count == maxfreq)

# Example usage:
nums = [1, 2, 2, 3, 3, 3]
print(maxFrequencyElements(nums))  # Output: 3

# Another example:
nums = [4, 4, 5, 5, 6, 6]
print(maxFrequencyElements(nums))  # Output: 6

# Yet another example:
nums = [7, 8, 8, 9, 9]
print(maxFrequencyElements(nums))  # Output: 4
