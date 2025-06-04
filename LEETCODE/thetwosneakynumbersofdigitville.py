# LEETCODE 3289

'''
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
Each number was supposed to appear exactly once in the list. However, two mischievous numbers sneaked in an additonal time,
making the list longer than usual.
As the town dectective, your task is to find these two sneaky numbers. 
Return an array of size two containing the two numbers (in any order), so peace an return to Digitville.
'''

from collections import Counter
def getSneakyNumbers(nums):
    sneaky = []
    
    frequency = Counter(nums)
    
    for key, value in frequency.items():
        if value > 1:
            sneaky.append(key)
    return sneaky

# Example usage:
nums = [0, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9]
print(getSneakyNumbers(nums))  # Output: [5, 6]

# Another example:
nums = [1, 2, 3, 4, 4, 5, 6, 6, 7]
print(getSneakyNumbers(nums))  # Output: [4, 6]

# Yet another example:
nums = [0, 1, 2, 2, 3, 4, 5, 5]
print(getSneakyNumbers(nums))  # Output: [2, 5]