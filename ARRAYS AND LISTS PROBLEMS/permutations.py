# Given two lists are the permutations of each other or not.

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    else:
        return False
    
# Example usage:
list1 = [1, 2, 3]
list2 = [3, 2, 1]
result = permutation(list1, list2)
print(result)  # Output: True

# Another example usage:
list3 = ['a', 'b', 'c']
list4 = ['c', 'b', 'a']
result2 = permutation(list3, list4)
print(result2)  # Output: True

# Yet another example usage:
list5 = [1, 2, 3, 4]
list6 = [1, 2, 4, 5]
result3 = permutation(list5, list6)
print(result3)  # Output: False
    