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


# Deleting an element from a dictionary

mydict4 = { 'name': 'Paul', 'age': 30, 'city': 'London' }

del mydict4['age']  # Delete the 'age' key-value pair
print(mydict4)  # Output: {'name': 'Paul', 'city': 'London'}
# Time Complexity: O(1)
# Space Complexity: O(1)

removedelement = mydict4.pop('city')  # Remove 'city' and return its value
print(removedelement)  # Output: London
print(mydict4)  # Output: {'name': 'Paul'}
# Time Complexity: O(1)
# Space Complexity: O(1)

mydict5 = { 'name': 'Alice', 'age': 25, 'city': 'Paris' }
deleteditem = mydict.popitem()
print(deleteditem)  # Output: ('city', 'Paris')
print(mydict5)  # Output: {'name': 'Alice', 'age': 25}
# Time Complexity: O(1)
# Space Complexity: O(1)

cleareddict = mydict5.clear()  # Clear the dictionary
print(cleareddict)  # Output: None
print(mydict5)  # Output: {}
# Time Complexity: O(n)
# Space Complexity: O(1)


# Dictionary Methods 

# 1. clear() method
dictionary1 = { 'name': 'Bob', 'age': 22, 'city': 'Berlin', 'job': 'Engineer'
            , 'country': 'Germany', 'hobby': 'Cycling' }
dictionary1.clear()  # Clear the dictionary
print(dictionary1)  # Output: {}
# Time Complexity: O(n)
# Space Complexity: O(1)


# 2. copy() method
dictionary2 = { 'name': 'Alice', 'age': 30, 'city': 'New York' }
dictionary3 = dictionary2.copy()  # Create a shallow copy of the dictionary
print(dictionary2)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Time Complexity: O(n)
# Space Complexity: O(n)


# 3. fromkeys() method 
# Syntax: dict.fromkeys(sequence[], value)
dictionary4 = dictionary2.fromkeys(['name', 'age', 'city'], ['Thomas', '35', 'Los Angeles'])
print(dictionary4)  # Output: {'name': ['Thomas', '35', 'Los Angeles'], 'age': ['Thomas', '35', 'Los Angeles'], 'city': ['Thomas', '35', 'Los Angeles']}
# Time Complexity: O(n)
# Space Complexity: O(n)


# 4. get() method
dictionary5 = { 'name': 'Charlie', 'age': 28, 'city': 'San Francisco' }
print(dictionary5.get('name'))  # Output: Charlie
print(dictionary5.get('country'))  # Output: None (key not found)
# Time Complexity: O(1)
# Space Complexity: O(1)


# 5. items() method
dictionary6 = { 'name': 'David', 'age': 32, 'city': 'Toronto' }
print(dictionary6.items())  # Output: dict_items([('name', 'David'), ('age', 32), ('city', 'Toronto')])
# Time Complexity: O(n)
# Space Complexity: O(1)


# 6. keys() method
dictionary7 = { 'name': 'Eva', 'age': 26, 'city': 'Sydney' }
print(dictionary7.keys())  # Output: dict_keys(['name', 'age', 'city'])
# Time Complexity: O(n)
# Space Complexity: O(1)


# 7. popitem() method
dictionary8 = { 'name': 'Frank', 'age': 29, 'city': 'Tokyo' }
popped_item = dictionary8.popitem()  # Remove and return the last inserted key-value pair
print(popped_item)  # Output: ('city', 'Tokyo')
print(dictionary8)  # Output: {'name': 'Frank', 'age': 29}
# Time Complexity: O(1)
# Space Complexity: O(1)


# 8. setdefault() method
dictionary9 = { 'name': 'Grace', 'age': 27 }
dictionary9.setdefault('city', 'London')  # Set default value for 'city' if not present
print(dictionary9)  # Output: {'name': 'Grace', 'age': 27, 'city': 'London'}

dictionary10 = { 'name': 'Hannah', 'age': 24 }
dictionary10.setdefault('city') # No default value provided, so 'city' will be set to None
print(dictionary10)  # Output: {'name': 'Hannah', 'age': 24, 'city': None}

dictionary11 = { 'name': 'Ian', 'age': 31 }
dictionary11.setdefault('age', 35)  # 'age' already exists, so it won't change
print(dictionary11)  # Output: {'name': 'Ian', 'age': 31}

# Time Complexity: O(1)
# Space Complexity: O(1)


# 9. pop() method
dictionary12 = { 'name': 'Jack', 'age': 33, 'city': 'Berlin' }
removed_value = dictionary12.pop('city')  # Remove 'city' and return its value
print(removed_value)  # Output: Berlin
print(dictionary12)  # Output: {'name': 'Jack', 'age': 33}
# Time Complexity: O(1)
# Space Complexity: O(1)


# 10. values() method
dictionary13 = { 'name': 'Kate', 'age': 25, 'city': 'Paris' }
print(dictionary13.values())  # Output: dict_values(['Kate', 25, 'Paris'])
# Time Complexity: O(n)
# Space Complexity: O(1)


# 11. update() method
dictionary14 = { 'name': 'Liam', 'age': 30 }
dictionary14.update({'city': 'Dublin', 'country': 'Ireland'})  # Update with new key-value pairs
print(dictionary14)  # Output: {'name': 'Liam', 'age': 30, 'city': 'Dublin', 'country': 'Ireland'}

dictionary14.update({'age': 35})  # Update existing key 'age'
print(dictionary14)  # Output: {'name': 'Liam', 'age': 35, 'city': 'Dublin', 'country': 'Ireland'}

d14 = dictionary14.update()
print(d14)  # Output: None

dictionary15 = { 'city': 'New York', 'country': 'USA' }
dictionary15.update(dictionary14)  # Update with another dictionary
print(dictionary15)  # Output: {'city': 'New York', 'country': 'USA', 'name': 'Liam', 'age': 35}
# Time Complexity: O(n)
# Space Complexity: O(n)


