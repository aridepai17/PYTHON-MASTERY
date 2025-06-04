# LEETCODE 2367 

'''
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
1. i < j < k
2. nums[j] - nums[i] == diff
3. nums[k] - nums[j] == diff
Return the number of unique arithmetic triplets.
'''

# Brute Force solution

def arithmeticTriplets(nums, diff):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    count += 1
    return count

# Optimal solution using set for O(n) complexity
def arithmeticTriplets(nums, diff):
    numset = set(nums)
    count = 0
    
    for num in nums:
        if (num + diff) in numset and (num + 2 * diff) in numset:
            count += 1
    return count

# Example usage:
nums = [0, 1, 4, 6, 7, 10]
diff = 3
print(arithmeticTriplets(nums, diff))  # Output: 2

# Another example:
nums = [4, 5, 6, 7, 8]
diff = 1
print(arithmeticTriplets(nums, diff))  # Output: 3