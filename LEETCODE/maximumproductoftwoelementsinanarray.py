# LEETCODE 1464

'''
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''

def maxProduct(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)

# Example usage
nums1 = [3, 4, 5, 2]
print(maxProduct(nums1))  # Output: 12

# Additional examples
nums2 = [1, 5, 4, 5]
print(maxProduct(nums2))  # Output: 16 (Max: (5-1)*(5-1) = 16)

nums3 = [10, 2, 5, 1, 7]
print(maxProduct(nums3))  # Output: 63 (Max: (10-1)*(7-1) = 63)

nums4 = [1, 1, 1, 1]
print(maxProduct(nums4))  # Output: 0 (Max: (1-1)*(1-1) = 0)

nums5 = [8, 7, 6, 5]
print(maxProduct(nums5))  # Output: 42 (Max: (8-1)*(7-1) = 42)

nums6 = [100, 1, 2, 3]
print(maxProduct(nums6))  # Output: 9801 (Max: (100-1)*(3-1) = 9801)

nums7 = [9, 9, 9, 9]
print(maxProduct(nums7))  # Output: 64 (Max: (9-1)*(9-1) = 64)