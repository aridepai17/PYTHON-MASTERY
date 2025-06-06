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

