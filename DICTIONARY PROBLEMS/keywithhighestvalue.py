# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

def max_value_key(my_dict):
    if not my_dict:
        return None
    maximum = max(my_dict, key = my_dict.get)
    return maximum

# Example usage:
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
max_key = max_value_key(dictionary)
print(max_key)  # Output: 'e'

# Another example usage:
dictionary = {'a': 8, 'b': 9, 'c': 17, 'd': 3, 'e': 11}
max_key = max_value_key(dictionary)
print(max_key)  # Output: 'c'