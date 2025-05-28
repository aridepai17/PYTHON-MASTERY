# Two Dimensional arrays

# Creating a 2D array using numpy

import numpy as np 

twoD = np.array([[11, 12, 13],
                [21, 22, 23],
                [31, 32, 33],
                [41, 42, 43],
                [51, 52, 53]])


# Inserting an element in a 2D array

newtwoD = np.insert(twoD, 0, [1, 2, 3, 4, 5], axis = 1)
print(newtwoD)
# Output:
# [ [ 1 11 12 13]
# [ 2 21 22 23]
# [ 3 31 32 33]
# [ 4 41 42 43]
# [ 5 51 52 53] ]

newtwoD = np.insert(twoD, 0, [1, 2, 3], axis = 0)
print(newtwoD)
# Output:
# [ [ 1 2 3 ]
# [ 11 12 13]
# [ 21 22 23]
# [ 31 32 33]
# [ 41 42 43]
# [ 51 52 53] ]


# Accessing an element in a 2D array

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Index out of range")
    else:
        print(array[rowIndex][colIndex])
        
accessElement(twoD, 2, 2)  # 33
accessElement(twoD, 5, 5)  # Index out of range
accessElement(twoD, 3, 0)  # 41


# Traverse a 2D array

def traversearray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
traversearray(twoD) 

    


                