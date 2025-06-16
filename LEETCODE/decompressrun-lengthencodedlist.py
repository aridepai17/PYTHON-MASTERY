# LEETCODE 1313

'''
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
For each such pair, there are freq elements with value val concatenated in a sublist. 
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.
'''

def decompressRLElist(nums):
    result = []
    
    for i in range(0, len(nums), 2):
        frequency = nums[i]
        value = nums[i + 1]
        result.extend([value] * frequency)
    return result

# Example usage
nums1 = [1, 2, 3, 4]
print(decompressRLElist(nums1))  # Output: [2, 4, 4, 4]

# Additional examples
nums2 = [1, 1, 2, 2]
print(decompressRLElist(nums2))  # Output: [1, 2, 2]

nums3 = [4, 5, 1, 6]
print(decompressRLElist(nums3))  # Output: [5, 5, 5, 5, 6]

nums4 = [2, 3, 3, 2]
print(decompressRLElist(nums4))  # Output: [3, 3, 2, 2]

nums5 = [3, 1, 2, 4]
print(decompressRLElist(nums5))  # Output: [1, 1, 1, 4, 4]

nums6 = [0, 5, 2, 6]
print(decompressRLElist(nums6))  # Output: [6, 6]

nums7 = [5, 0]
print(decompressRLElist(nums7))  # Output: [] (No values to decompress)