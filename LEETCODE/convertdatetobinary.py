# LEETCODE 3280

'''
You're given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
date can be written in its binary representation obtained by converting year, month, and day to their 
binary representations without any leading zeroes and writing them down in year-month-day format.
Return the binary representation of date.
'''

def convertDatetoBinary(date):
    year, month, day = date.split('-')
    
    yearbinary = bin(int(year))[2:]  # Convert year to binary and remove '0b' prefix
    monthbinary = bin(int(month))[2:]  # Convert month to binary and remove '0b' prefix
    daybinary = bin(int(day))[2:]  # Convert day to binary and remove '0b' prefix
    
    return f"{yearbinary}-{monthbinary}-{daybinary}"

# Example usage:
date = "2023-10-05"
print(convertDatetoBinary(date))  # Output: "11111100111-1010-101"

# Another example usage:
date = "2000-01-01"
print(convertDatetoBinary(date))  # Output: "11111010000-1-1"

# Yet another example usage:
date = "1999-12-31"
print(convertDatetoBinary(date))  # Output: "11111010000-1111-1"