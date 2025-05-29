# Find the maximum product of two integers in an array where all elements are positive.

def max_product(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

# Example usage:
arr = [1, 2, 3, 4, 5]
result = max_product(arr)
print(result)  # Output: 20 (4 * 5)

# Another example usage:
arr2 = [10, 20, 30, 40]
result2 = max_product(arr2) 
print(result2)  # Output: 1200 (30 * 40)