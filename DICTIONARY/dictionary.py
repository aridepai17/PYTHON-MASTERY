# Creating a dictionary 

mydict = dict()
print(mydict)

mydict2 = {}
print(mydict2)

eng_sp = dict(one='uno', two='dos', three='tres',
            four='cuatro', five='cinco', six='seis',
            seven='siete', eight='ocho', nine='nueve',
            ten='diez')
print(eng_sp)

eng_sp2 = { 'one': 'uno', 'two': 'dos', 'three': 'tres',
            'four': 'cuatro', 'five': 'cinco', 'six': 'seis',
            'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve',
            'ten': 'diez' }
print(eng_sp2)

eng_sp3 = [('one', 'uno'), ('two', 'dos'), ('three', 'tres'),
            ('four', 'cuatro'), ('five', 'cinco'), ('six', 'seis'), 
            ('seven', 'siete'), ('eight', 'ocho'), ('nine', 'nueve'),
            ('ten', 'diez')]
mydict3 = dict(eng_sp3)
print(mydict3)
# Time Complexity: O(n)
# Space Complexity: O(n)


# Insertion / Updation of dictionary

myDict = {'name': 'Eddy', 'age': 26}
myDict['age'] = 27  # Update age
print(myDict) # Output: {'name': 'Eddy', 'age': 27}
# Time Complexity: O(1)
# Space Complexity: O(1)

myDict['city'] = 'New York'  # Add new key-value pair
print(myDict)  # Output: {'name': 'Eddy', 'age': 27, 'city': 'New York'}
myDict['country'] = 'USA'  # Add another new key-value pair
print(myDict)  # Output: {'name': 'Eddy', 'age': 27, 'city': 'New York', 'country': 'USA'}
# Time Complexity: O(1)
# Space Complexity: O(1)


# Traversing through a dictionary

dict1 = {'name': 'Cristiano', 'age': 40, 'team': 'Al Nassr'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
        
traverseDict(dict1)
# Output:
# name Cristiano
# age 40
# team Al Nassr

# Time Complexity: O(n)
# Space Complexity: O(1)


# Searching for an element in a dictionary

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Not Found"

searchDict(dict1, 'Cristiano')  # Output: ('name', 'Cristiano')
searchDict(dict1, 'Lionel')  # Output: Not Found

# Time Complexity: O(n)
# Space Complexity: O(1)