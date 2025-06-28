# LEETCODE 1154

'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
'''

def dayOfYear(date):
    year, month, day = map(int, date.split('-'))
    
    # Days in each month for a non-leap year
    daysinMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        daysinMonth[1] = 29
    
    # Calculate the day of the year
    return sum(daysinMonth[:month - 1]) + day

# Example usage:
date = "2019-01-09"
print(dayOfYear(date))  # Output: 9

date2 = "2019-02-10"
print(dayOfYear(date2))  # Output: 41

date3 = "2003-03-01"
print(dayOfYear(date3))  # Output: 60

date4 = "2004-03-01"
print(dayOfYear(date4))  # Output: 61

date5 = "2000-02-29"
print(dayOfYear(date5))  # Output: 60

# New examples
new_date1 = "2020-01-01"
print(dayOfYear(new_date1))  # Output: 1

new_date2 = "2020-12-31"
print(dayOfYear(new_date2))  # Output: 366

new_date3 = "2021-07-15"
print(dayOfYear(new_date3))  # Output: 196

new_date4 = "2022-02-28"
print(dayOfYear(new_date4))  # Output: 59

new_date5 = "2023-03-01"
print(dayOfYear(new_date5))  # Output: 60