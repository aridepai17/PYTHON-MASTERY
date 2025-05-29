# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(lst):
    return lst[1:-1]

# Example usage:
example_list = [1, 2, 3, 4, 5]
result = middle(example_list)
print(result) # Output: [2, 3, 4]

# Another example usage:
another_list = ['a', 'b', 'c', 'd', 'e']
another_result = middle(another_list)
print(another_result) # Output: ['b', 'c', 'd']