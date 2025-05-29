# Write a function to remove the duplicate numbers on the given array/list

def remove_duplicates(arr):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# Example usage:
arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print(result)  # Output: [1, 2, 3, 4, 5]

# Another example usage:
arr2 = [10, 20, 20, 30, 30, 40]
result2 = remove_duplicates(arr2)
print(result2)  # Output: [10, 20, 30, 40]