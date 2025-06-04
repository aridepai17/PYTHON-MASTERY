# LEETCODE 1672

'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has
in the j-th bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
'''

def maximumWealth(accounts):
    return max(sum(customers) for customers in accounts)

# Example usage:
accounts = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
print(maximumWealth(accounts))  # Output: 15

# Another example:
accounts = [[1, 5], [7, 3], [3, 5]]
print(maximumWealth(accounts))  # Output: 10

# Yet another example:
accounts = [[2, 8, 7], [1, 9, 5], [3, 6, 4]]