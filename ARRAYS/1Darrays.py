import array

myarray = array.array('i')
print(myarray) # array('i')

myarray1 = array.array('i', [1, 2, 3, 4, 5])
print(myarray1) # array('i', [1, 2, 3, 4, 5])

import numpy as np

myarray2 = np.array([], dtype=int)
print(myarray2) # []

myarray3 = np.array([1, 2, 3, 4, 5])
print(myarray3) # [1 2 3 4 5]

# Time complexity is O(1)
# Space complexity is O(n)


# Inserting elements in an array

myarray3.insert(0, 6)  # Insert 6 at index 0
print(myarray3)  # [6 1 2 3 4 5]

myarray3.insert(2, 7)  # Insert 7 at index 2
print(myarray3)  # [6 1 7 2 3 4 5]

myarray3.insert(7, 8)  # Insert 8 at index 7
print(myarray3)  # [6 1 7 2 3 4 5 8]

# Time complexity is O(n)
# Space complexity is O(n)


# Traversal operation in array
def traversearray(myarray3):
    for i in myarray3:
        print(i)
        
traversearray(myarray3)  # 6 1 7 2 3 4 5 8

# Time complexity is O(n)
# Space complexity is O(n)


# Acessing elements in an array
arr1 = np.array([1, 2, 3, 4, 5])

def accessElement(arr1, index):
    if index > len(arr1):
        print("Index out of range")
    else:
        print(arr1[index])
        
accessElement(arr1, 2)  # 3 
accessElement(arr1, 5)  # Index out of range

# Time complexity is O(1)
# Space complexity is O(1)


# Searching for an element in an array
arr2 = np.array([1, 2, 3, 4, 5])

def linearSearch(arr2, element):
    for i in range(len(arr2)):
        if arr2[i] == element:
            return i
    return "Element not found"

print(linearSearch(arr2, 3))  # 2
print(linearSearch(arr2, 6))  # Element not found

# Time complexity is O(n)
# Space complexity is O(1)


# Deleting an element from an array
arr3 = np.array([1, 2, 3, 4, 5])

arr3.remove(3)  # Remove the first occurrence of 3
print(arr3)  # [1 2 4 5]

arr3.remove(5)  # Remove the first occurrence of 5
print(arr3)  # [1 2 4]

# Time complexity is O(n)
# Space complexity is O(1)

        
        


