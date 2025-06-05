# LEETCODE 2574

'''
You are given a 0-indexed integer array nums of size n.
Define two arrays leftSum and rightSum where:
- leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
- rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
'''

def leftRightDifference(nums):
    leftsum = 0
    rightsum = sum(nums)
    result = []
    
    for num in nums:
        rightsum -= num
        result.append(abs(leftsum - rightsum))
        leftsum += num
    return result

# Example usage:
nums = [10, 4, 8, 3]
print(leftRightDifference(nums))  # Output: [15, 1, 11, 22]

# Another example:
nums = [1, 2, 3, 4, 5]
print(leftRightDifference(nums))  # Output: [14, 11, 6, 1, 10]

# Yet another example:
nums = [5, 10, 15]
print(leftRightDifference(nums))  # Output: [25, 10, 15]