# LEETCODE 1360

'''
Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
'''

from datetime import datetime

def daysBetweenDates(date1, date2):
    # Parse the input date strings into datetime objects
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    
    # Calculate the difference in days
    return abs((d2 - d1).days)
  
# Alternate solution

def daysBetweenDatesAlternate(date1, date2):
    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))
    
    return abs((datetime.date(y1, m1, d1) - datetime.date(y2, m2, d2)).days)
  
# Example usage
date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))  # Output: 1

# Additional examples
print(daysBetweenDates("2020-01-01", "2020-01-31"))  # Output: 30
print(daysBetweenDates("2020-12-31", "2021-01-01"))  # Output: 1
print(daysBetweenDates("2018-05-15", "2018-05-15"))  # Output: 0
print(daysBetweenDates("2000-01-01", "2020-01-01"))  # Output: 7305
print(daysBetweenDates("2024-02-28", "2024-03-01"))  # Output: 2 (leap year)
print(daysBetweenDates("2023-03-01", "2023-02-28"))  # Output: 1
print(daysBetweenDates("1999-12-31", "2000-01-01"))  # Output: 1
print(daysBetweenDates("2022-01-01", "2022-12-31"))  # Output: 364
print(daysBetweenDates("2021-07-20", "2021-08-20"))  # Output: 31