# LEETCODE 13

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.

def romanToInt(s):
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    total = 0
    prev = 0
    
    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value 
        prev = value
    return total

# Example usage:
s = "III"
print(romanToInt(s))  # Output: 3

# Another example usage:
s = "XXXIX"
print(romanToInt(s))  # Output: 39

# Yet another example usage:
s = "LVIII"
print(romanToInt(s))  # Output: 58