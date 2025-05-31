# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

def merge_dicts(dict1, dict2):
    merge = dict1.copy()
    for key, value in dict2.items():
        if key in merge:
            merge[key] += value
        else:
            merge[key] = value
    return merge

# Example usage:
dictionary01 = {'a': 1, 'b': 2, 'c': 3}
dictionary02 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dictionary01, dictionary02)
# Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# Another usage:
dictionary03 = {'a': 5, 'b': 8, 'c': 5}
dictionary04 = {'b': 2, 'c': 8, 'd': 1}
merge_dicts(dictionary03, dictionary04)
# Output: {'a': 5, 'b': 10, 'c': 13, 'd': 1}

