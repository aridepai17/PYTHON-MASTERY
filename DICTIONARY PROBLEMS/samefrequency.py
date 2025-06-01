# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

def same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
    
    frequency1 = {}
    frequency2 = {}
    
    for keys in list1:
        frequency1[keys] = frequency1.get(keys, 0) + 1
        
    for keys in list2:
        frequency2[keys] = frequency2.get(keys, 0) + 1
        
    return frequency1 == frequency2

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print(same_frequency(list1, list2))  # Output: True

# Another example usage:
list1 = [1, 2, 2, 4, 5, 6]
list2 = [5, 4, 3, 2, 1, 6]
print(same_frequency(list1, list2))  # Output: False



