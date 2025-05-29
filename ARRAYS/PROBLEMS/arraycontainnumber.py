# Checking if array contains specified number
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
            
# Example usage:
findNumber(myArray, 5)  # Output: 4
findNumber(myArray, 11)  # No output, since 11 is not in the array