# Given a list, write a function to get first, second best scores from the list. List may contain duplicates.

def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
    
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1, max2

# Example usage:
my_list = [10, 20, 20, 30, 40, 40]
result = first_second(my_list)
print(result)  # Output: (40, 30)

# Another example usage:
my_list2 = [77, 88, 88, 99, 99, 100]
result2 = first_second(my_list2)
print(result2)  # Output: (100, 99)