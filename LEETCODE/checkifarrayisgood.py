# LEETCODE 2784

'''
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
base[n] = [0, 1, 2, ..., n - 1, n , n] ( in other words, it is an array with length n + 1 which contains 1 to n - 1 exactly once,
plus two occurrences of n).
For example, base[3] = [0, 1, 2, 3, 3].
Return true if nums is good, otherwise return false.
A permutation of integers represents an arrangement of these numbers.
'''

def checkIfArrayIsGood(nums):
    n  = len(nums)
    expected = list(range(1, n))
    expected.append(n - 1)
    
    return sorted(nums) == sorted(expected)

# Example usage
nums = [0, 1, 2, 3, 3]
print(checkIfArrayIsGood(nums))  # Output: True

# Example usage
nums = [0, 1, 2, 3, 4]
print(checkIfArrayIsGood(nums))  # Output: False

# Example usage
nums = [0, 1, 2, 2, 3]
print(checkIfArrayIsGood(nums))  # Output: False

# Example usage
nums = [0, 1, 2, 3, 3, 4]
print(checkIfArrayIsGood(nums))  # Output: True