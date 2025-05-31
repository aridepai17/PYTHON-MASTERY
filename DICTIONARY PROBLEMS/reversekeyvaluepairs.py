# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

def reversekeyvaluepairs(mydict):
    return { value : key for key, value in mydict.items()}

# Example usage:
mydict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reversekeyvaluepairs(mydict)
print(reversed_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Another example usage:
mydict2 = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
reversed_dict2 = reversekeyvaluepairs(mydict2)
print(reversed_dict2)  # Output: {'Alice': 'name', 25: 'age', 'Paris': 'city'}

# Yet another example usage:
mydict3 = {'x': 10, 'y': 20, 'z': 30}
reversed_dict3 = reversekeyvaluepairs(mydict3)
print(reversed_dict3)  # Output: {10: 'x', 20: 'y', 30: 'z'}