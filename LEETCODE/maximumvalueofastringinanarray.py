# LEETCODE 2496

'''
The value of an alphanumeric string can be defined as:
- The numeric representation of the string in base 10, if it comprises of digits only.
- The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs
'''

def maximumValue(strs):
    maximumvalue = 0
    
    for s in strs:
        if s.isdigit():
            value = int(s)
        else:
            value = int(len(s))
        maximumvalue = max(maximumvalue, value)
    return maximumvalue

# Example usage:
strs = ["1", "01", "001", "0001"]
print(maximumValue(strs))  # Output: 1

# Example usage:
strs = ["abc", "ab", "a"]
print(maximumValue(strs))  # Output: 3

# Example usage:
strs = ["123", "4567", "89"]
print(maximumValue(strs))  # Output: 4567

# Example usage:
strs = ["hello", "world", "python"]
print(maximumValue(strs))  # Output: 6