# LEETCODE 1365

'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
'''

def smallerNumbersThanCurrent(nums):
    sortedNums = sorted(nums)
    smallerCount = {}
    
    for index, value in enumerate(sortedNums):
        if value not in smallerCount:
            smallerCount[value] = index
    
    result = []  
    for value in nums:
        result.append(smallerCount[value])  
    
    return result 

# Examples usage
nums1 = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums1))  # Output: [4, 0, 1, 1, 3]

# Additional examples
nums2 = [6, 5, 4, 8]
print(smallerNumbersThanCurrent(nums2))  # Output: [2, 1, 0, 3]

nums3 = [7, 7, 7, 7]
print(smallerNumbersThanCurrent(nums3))  # Output: [0, 0, 0, 0]

nums4 = [1, 0, 2, 3, 4]
print(smallerNumbersThanCurrent(nums4))  # Output: [1, 0, 2, 3, 4]

nums5 = [10, 20, 10, 30, 20]
print(smallerNumbersThanCurrent(nums5))  # Output: [2, 4, 2, 4, 4]

num6 = [5, 3, 8, 6, 2]
print(smallerNumbersThanCurrent(num6))  # Output: [2, 1, 4, 3, 0]