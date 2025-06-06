# Creating a tuple 
newTuple1 = (1, 2, 3, 4, 5)
print(newTuple1) # Output: (1, 2, 3, 4, 5)

# Creation of single element tuple
newTuple2 = (1,)  # Note the comma
print(newTuple2)  # Output: (1,)

# Creating tuple using tuple() constructor
newTuple3 = tuple([6, 7, 8])
print(newTuple3)  # Output: (6, 7, 8)

newTuple4 = tuple('abcde')
print(newTuple4)  # Output: ('a', 'b', 'c', 'd', 'e')

newTuple5 = tuple(range(10))
print(newTuple5)  # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Time Complexity : O(1)
# # Space Complexity : O(n) where n is the number of elements in the tuple



# Accessing elements in a tuple
newTuple6 = (10, 20, 30, 40, 50)
print(newTuple6[0])  # Output: 10
print(newTuple6[-1])  # Output: 50
print(newTuple6[1:4])  # Output: (20, 30, 40)
print(newTuple6[:3])  # Output: (10, 20, 30)
print(newTuple6[2:])  # Output: (30, 40, 50)
print(newTuple6[3::-1])  # Output: (40, 30, 20, 10)

# Time Complexity : O(1) for accessing a single element
# Space Complexity : O(n) where n is the number of elements in the tuple


# Traversing a tuple
newTuple7 = (1, 2, 3, 4, 5)
for i in newTuple7:
    print(i) # Output: 1 2 3 4 5
    
for i in range(len(newTuple7)):
    print(newTuple7[i])  # Output: 1 2 3 4 5

# Time Complexity : O(n) where n is the number of elements in the tuple
# Space Complexity : O(1) for the loop variable, O(n) for the tuple itself


# Searching elements in a tuple
newTuple8 = (1, 2, 3, 4, 5)
print(3 in newTuple8)  # Output: True
print(6 in newTuple8)  # Output: False
print(newTuple8.index(3))  # Output: 2
print(newTuple8.index(6))  # Raises ValueError if 6 is not found

def searchTuple(newtuple, element):
    if element in newtuple:
        return newtuple.index(element)
    else:
        return -1
    
# Example usage:
newTuple9 = (1, 2, 3, 4, 5)
print(searchTuple(newTuple9, 3))  # Output: 2
print(searchTuple(newTuple9, 6))  # Output: -1

# Time Complexity : O(n) for searching an element
# Space Complexity : O(1) for the search operation, O(n) for the tuple itself


# Tuple operations and functions
myTuple10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
myTuple11 = (11, 12, 13, 14, 15)

print(myTuple10 + myTuple11)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) # Concatenation using the + operator

print(myTuple10 * 2)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Repetition using the * operator

print(len(myTuple10))  # Output: 10 # Length of the tuple using len() function

print(max(myTuple10))  # Output: 10 # Maximum element in the tuple using max() function

print(min(myTuple10))  # Output: 1 # Minimum element in the tuple using min() function

print(sum(myTuple10))  # Output: 55 # Sum of all elements in the tuple using sum() function

print(4 in myTuple10)  # Output: True # Checking if an element exists in the tuple using 'in' operator

print(myTuple10.count(4))  # Output: 1 # Counting occurrences of an element in the tuple using count() method

print(myTuple10.index(4))  # Output: 3 # Finding the index of an element in the tuple using index() method

print(any(myTuple10))  # Output: True # Checking if any element in the tuple is True using any() function

print(all(myTuple10))  # Output: True # Checking if all elements in the tuple are True using all() function

print(sorted(myTuple10))  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Sorting the tuple using sorted() function

print(enumerate(myTuple10))  # Output: <enumerate object at ...> # Enumerating the tuple using enumerate() function