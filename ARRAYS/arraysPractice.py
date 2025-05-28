import array
import numpy as np

# Practice problems for arrays in Python

#1. Create an array and traverse 

arr1 = np.array([10, 20, 30, 40, 50])
for i in arr1:
    print(i)
# Output: 10 20 30 40 50


#2. Access individual elements in an array through indexes

print(arr1[0])  # Output: 10
print(arr1[1])  # Output: 20
print(arr1[2])  # Output: 30
print(arr1[3])  # Output: 40
print(arr1[4])  # Output: 50

#3. Append any value to the array using append() method

arr1.append(60)
print(arr1)  # Output: [10 20 30 40 50 60]
arr1.append(70)
print(arr1)  # Output: [10 20 30 40 50 60 70]


#4. Insert value in an array using the insert() method

arr1.insert(0, 5)  # Insert 5 at index 0
arr1.insert(2, 25) # Insert 25 at index 2
arr1.inser(7, 80)  # Insert 80 at index 7
print(arr1)  # Output: [5 10 25 20 30 40 50 60 70 80]


#5. Extend the python array using extend() method

arr1.extend(90) # Extend the array with a single value
print(arr1)  # Output: [5 10 25 20 30 40 50 60 70 80 90]

arr1.extend([100, 110])  # Extend the array with multiple values
print(arr1)  # Output: [5 10 25 20 30 40 50 60 70 80 90 100 110]

arr1.extend([120, 130, 140])  # Extend the array with more values
print(arr1)  # Output: [5 10 25  0 30  40 50 60 70 80 90 100 110 120 130 140]


#6. Add items from list into array using fromlist() method

list1 = [150, 160, 170]
arr1.fromlist(list1)  # Add items from list to the array
print(arr1)  # Output: [ 5 10 25 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170]


#7. Remove any array element using remove() method

arr1.remove(25)  # Remove the first occurrence of 25
arr1.remove(50)  # Remove the first occurrence of 50
arr1.remove(170)  # Remove the first occurrence of 170
arr1.remove(160)  # Remove the first occurrence of 160
print(arr1)  # Output: [5 10 20 30 40 60 70 80 90 100 110 120 130 140 150]


#8. Remove last array element using pop() method

arr1.pop()  # Remove the last element (150)
arr1.pop()  # Remove the new last element (140)
print(arr1)  # Output: [5 10 20 30 40 60 70 80 90 100 110 120 130]


#9. Fetch any element through its index using index() method

arr1.index(20)  # Get the index of the first occurrence of 20
print(arr1.index(20))  # Output: 2

arr1.index(100) # Get the index of the first occurrence of 100
print(arr1.index(100))  # Output: 8

arr1.index(130)  # Get the index of the first occurrence of 130
print(arr1.index(130))  # Output: 11


#10. Reverse a python array using reverse() method

arr1.reverse()  # Reverse the array
print(arr1)  # Output: [130 120 110 100 90 80 70 60 40 30 20 10 5]


#11. Get array buffer information using buffer_info() method

bufferInfo = arr1.buffer_info() # Get buffer information
print(bufferInfo)  # Output: (address, size)


#12. Check for the number of occurrences of an element using count() method

count20 = arr1.count(20)  # Count occurrences of 20
count30 = arr1.count(30)  # Count occurrences of 30
print(count20)  # Output: 1
print(count30)  # Output: 1


#13. Convert an array to a string using tostring() method

arrstr = arr1.tostring() # Convert array to string
print(arrstr)   
# tostring() and fromstring() methods are deprecated in Python 3.90 and later


#14. Convert array to python list with the same elements using tolist() method

arrlist = arr1.tolist()  # Convert array to list
print(arrlist)  # Output: [130, 120, 110, 100, 90, 80, 70, 60, 40, 30, 20, 10, 5]


#15. Slice elements from an array using slice() method

print(arr1[2:5])  # Slice elements from index 2 to 5 (exclusive)
# Output: [110 100 90]

print(arr1[2:]) # Slice elements from index 2 to the end
# Output: [110 100 90 80 70 60 40 30 20 10 5]

print(arr1[:6]) # Slice elements from the start to index 6 (exclusive)
# Output: [130 120 110 100 90 80]

print(arr1[:]) # Slice all elements
# Output: [130 120 110 100 90 80 70 60 40 30 20 10 5]

print(arr1[-3:]) # Slice the last three elements
# Output: [20 10 5]

print(arr1[:-3]) # Slice all elements except the last three
# Output: [130 120 110 100 90 80 70 60 40 30]









