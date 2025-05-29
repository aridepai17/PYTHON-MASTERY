# Creating a list

list1 = [10, 20, 30, 40, 50] # List of integers
list2 = ['Milk', 'Eggs', 'Bread', 'Butter', 'Cheese'] # List of strings
list3 = [1, 1.5, 'Pepper'] # Mixed data types
list4 = ['Tomato', 2, 4.6, ['Onion', 'Garlic'], 5.5] # Nested list


# Accessing/Traversing a list

print(list1[0])  # Output: 10
print(list2[1])  # Output: Eggs
print(list3[2])  # Output: Pepper
print(list4[3][1])  # Output: Garlic

for i in list1:
    print(i) # Output: 10 20 30 40 50
    
    
# Updating/Inserting elements in a list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist[0] = 11  # Update first element
mylist[1] = 12  # Update second element
mylist[2] = 13  # Update third element
print(mylist)  # Output: [11, 12, 13, 4, 5, 6, 7, 8, 9, 10]

# Inserting element to beginning of the list
# Inserting an element to any given place on the list
# Inserting an element to the end of the list
# Inserting another list to the list

# List Methods for insertion of elements

# 1. insert()
mylist.insert(0, 0)  # Insert 0 at the beginning
mylist.insert(3, 3.5)  # Insert 3.5 at index 3
mylist.insert(5, 5.5)  # Insert 5.5 at index 5
print(mylist)  # Output: [0, 11, 12, 3.5, 13, 5.5, 6, 7, 8, 9, 10]

# 2. append()
mylist.append(11)  # Append 11 to the end of the list
mylist.append(12)  # Append 12 to the end of the list
mylist.append(15) # Append 15 to the end of the list
print(mylist)  # Output: [0, 11, 12, 3.5, 13, 5.5, 6, 7, 8, 9, 10, 11, 12, 15]

# 3. extend()
newlist = [19, 20]

mylist.extend([16, 17, 18])  # Extend the list with multiple values
print(mylist)  # Output: [0, 11, 12, 3.5, 13, 5.5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18]

mylist.extend(newlist)  # Extend the list with another list
print(mylist)  # Output: [0, 11, 12, 3.5, 13, 5.5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20]


# Slice/Delete element from the list

# 1. Using slice[:]
list01 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(list01[:5])  # Output: ['a', 'b', 'c', 'd', 'e']
print(list01[5:])  # Output: ['f', 'g', 'h', 'i', 'j']
print(list01[2:7])  # Output: ['c', 'd', 'e', 'f', 'g']

list01[2:5] = ['x', 'y', 'z']  # Replace elements at index 2, 3, 4 with 'x', 'y', 'z'
print(list01)  # Output: ['a', 'b', 'x', 'y', 'z', 'f', 'g', 'h', 'i', 'j']

# List methods for deletion

# 1. pop()
list01.pop()  # Remove the last element ('j')
list01.pop(1)  # Remove the element at index 1 ('b')
print(list01)  # Output: ['a', 'x', 'y', 'z', 'f', 'g', 'h', 'i']

# 2. delete()
del list01[0]  # Delete the element at index 0 ('a')
del list01[2:4]  # Delete elements at index 2 and 3 ('z', 'f')
print(list01)  # Output: ['x', 'y', 'g', 'h', 'i']

# 3. remove()
list01.remove('x')  # Remove the first occurrence of 'x'
list01.remove('i')  # Remove the first occurrence of 'i'
print(list01)  # Output: ['y', 'g', 'h']


# Searching for an element in a list
yourlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Using 'in' operator
target = 9
if target in yourlist:
    print(f"{target} is found in the list.")
else:
    print(f"{target} is not found in the list.")
    
# 2. Linear Search
def linearsearch(plist, ptarget):
    for i, value in enumerate(plist):
        if value == ptarget:
            return f"{ptarget} found at index {i}"
    return f"{ptarget} not found in the list."

print(linearsearch(yourlist, 5))  # Output: 5 found at index 4
print(linearsearch(yourlist, 11))  # Output: 11 not found in the list.


# List Operations and Functions

# 1. + operator for concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # Concatenate lists a and b
print(c)  # Output: [1, 2, 3, 4, 5, 6]

# 2. * operator for repetition
d = a * 2  # Repeat list a twice
print(d)  # Output: [1, 2, 3, 1, 2, 3]
e = b * 3  # Repeat list b three times
print(e)  # Output: [4, 5, 6, 4, 5, 6, 4, 5, 6]

# 3. len() function returns the count of elements in a list (length of the list)
print(len(c))  # Output: 6
print(len(d))  # Output: 6
print(len(e))  # Output: 9

# 4. max() function returns the maximum value in a list
print(max(c))  # Output: 6
print(max(d))  # Output: 3
print(max(e))  # Output: 6

# 5. min() function returns the minimum value in a list
print(min(c))  # Output: 1
print(min(d))  # Output: 1
print(min(e))  # Output: 4

# 6. sum() function returns the sum of all elements in a list
print(sum(c))  # Output: 21
print(sum(d))  # Output: 6
print(sum(e))  # Output: 18

# 7. sorted() function returns a new sorted list from the elements of the original list
f = [3, 1, 4, 2]
g = sorted(f)  # Sort the list f
print(g)  # Output: [1, 2, 3, 4]

# Strings and Lists functions

# 1. list() function converts a string to a list
a = "Hello"
b = list(a) # Convert string 'Hello' to a list of characters
print(b)  # Output: ['H', 'e', 'l', 'l', 'o']

# 2. split() method splits a string into a list of substrings
a = "Hello Python Programming"
b = a.split()  # Split the string into a list of words
print(b)  # Output: ['Hello', 'Python', 'Programming']

c = 'spam1-spam2-spam3'
delimiter = '-'
d = c.split(delimiter)  # Split the string using '-' as a delimiter
print(d)  # Output: ['spam1', 'spam2', 'spam3']

# 3. join() method joins a list of strings into a single string
e = ['Hello', 'Python', 'Programming']
f = ' '.join(e)  # Join the list of strings with a space
print(f)  # Output: Hello Python Programming


# List Comprehensions

# 1. new_list = [new_item for item in prev_list] 
prev_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in prev_list]  # Create a new list with each element multiplied by 2
print(prev_list)  # Output: [1, 2, 3, 4, 5]
print(new_list)  # Output: [2, 4, 6, 8, 10]

# 2. new_list = [letter for word in old_list] 
old_list = ['Hello World']
new_list = [letter for word in old_list for letter in word]  # Create a new list with each letter from the words
print(old_list)  # Output: ['Hello']
print(new_list)  # Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# 3. new_list = [new_item for item in prev_list if condition]
previous_list = [ -1, 10, 35, -20, 50, 60, -70]
new_list = [x for x in previous_list if x > 0]  # Create a new list with only positive numbers
print(previous_list)  # Output: [-1, 10, 35, -20, 50, 60, -70]
print(new_list)  # Output: [10, 35, 50, 60]

# Another example of list comprehension with a condition
sentence = "My name is Advaith"
def isConsonant(letter):
    vowels = 'aeiou'
    return letter.lower() not in vowels and letter.isalpha()

consonants = [letter for letter in sentence if isConsonant(letter)]  # Create a list of consonants from the sentence
print(consonants)  # Output: ['M', 'y', 'n', 'm', 's', 'd', 'v', 't', 'h']
















