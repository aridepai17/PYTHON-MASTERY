# LEETCODE 2798

'''
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
The company requires each employee to work for at least target hours.
You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
Return the integer denoting the number of employees who worked at least target hours.
'''

def numberOfEmployeesWhoMetTarget(hours, target):
    count = 0
    for num in hours:
        if num >= target:
            count += 1
    return count 

# Example usage:
hours = [40, 35, 45, 50, 30]
target = 40
print(numberOfEmployeesWhoMetTarget(hours, target))  # Output: 3

# Another example:
hours = [20, 25, 30, 15, 10]
target = 20
print(numberOfEmployeesWhoMetTarget(hours, target))  # Output: 3

# Yet another example:
hours = [10, 15, 20, 25]
target = 30
print(numberOfEmployeesWhoMetTarget(hours, target))  # Output: 0