# LEETCODE 1470

'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result

# Example usage
nums = [2, 5, 1, 3, 4, 7]
n = 3
print(shuffle(nums, n))  # Output: [2, 3, 5, 4, 1, 7]

# Another example usage
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(shuffle(nums, n))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]

# Yet another example usage
nums = [1, 1, 2, 2]
n = 2
print(shuffle(nums, n))  # Output: [1, 2, 1, 2]