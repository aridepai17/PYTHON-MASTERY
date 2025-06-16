# LEETCODE 2553

'''
Given an array of positive integers nums, 
return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
'''

def separateDigits(nums):
    result = []
    
    for num in nums:
        for digit in str(num):
            result.append(int(digit))
    return result

# Example usage
nums1 = [123, 456, 789]
print(separateDigits(nums1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nums2 = [10, 20, 30]
print(separateDigits(nums2))  # Output: [1, 0, 2, 0, 3, 0]

# Additional examples
nums3 = [5, 12, 34]
print(separateDigits(nums3))  # Output: [5, 1, 2, 3, 4]

nums4 = [100, 200, 300]
print(separateDigits(nums4))  # Output: [1, 0, 0, 2, 0, 0, 3, 0, 0]

nums5 = [9, 8, 7, 6]
print(separateDigits(nums5))  # Output: [9, 8, 7, 6]

nums6 = [12345, 67890]
print(separateDigits(nums6))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

nums7 = [0, 1, 2, 3]
print(separateDigits(nums7))  # Output: [0, 1, 2, 3]

nums8 = [1001, 2020, 3030]
print(separateDigits(nums8))  # Output: [1, 0, 0, 1, 2, 0, 2, 0, 3, 0, 3, 0]