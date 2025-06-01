# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition that the value is even.

def conditional_filter(mydict):
    return { key : value for key, value in mydict.items() if value % 2 == 0 }

# Example usage:
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(conditional_filter(mydict))  # Output: {'b': 2, 'd': 4}

# Another example usage:
mydict = {'a': 8, 'b': 9, 'c': 13, 'd': 6, 'e': 14}
print(conditional_filter(mydict))  # Output: {'a': 8, 'd': 6, 'e': 14}



