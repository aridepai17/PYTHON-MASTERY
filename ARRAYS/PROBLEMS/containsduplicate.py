# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Example usage:
nums1 = [1, 2, 3, 1]
result1 = contains_duplicate(nums1)
print(result1)  # Output: True

# Another example usage:
nums2 = [1, 2, 3, 4]
result2 = contains_duplicate(nums2)
print(result2)  # Output: False