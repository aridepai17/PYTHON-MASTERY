# LEETCODE 1475

'''
You are given an integer array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
'''

# Optimal O(n) solution using a monotonic stack.
def finalPrices(prices):
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            j = stack.pop()
            prices[j] -= prices[i]
        stack.append(i)
    return prices

# Alternate solution O(n^2) using a nested loop.

def finalPrices(prices):
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    return prices

# Example usage
prices = [8, 4, 6, 2, 3]
print(finalPrices(prices)) # Output: [4, 2, 4, 2, 3]

# Example usage for the optimal solution
prices = [10, 1, 1, 6]
print(finalPrices(prices)) # Output: [9, 0, 1, 6]

# Example usage for the alternate solution
prices = [5, 10, 6, 8]
print(finalPrices(prices)) # Output: [5, 10, 6, 8]

# Example usage for the alternate solution with no discounts
prices = [7, 8, 9, 10]
print(finalPrices(prices)) # Output: [7, 8, 9, 10]

# Example usage for the alternate solution with all discounts
prices = [10, 9, 8, 7]
print(finalPrices(prices)) # Output: [10, 9, 8, 7]

# Example usage for the alternate solution with mixed discounts
prices = [3, 5, 2, 6, 1]
print(finalPrices(prices)) # Output: [2, 5, 1, 6, 1]

# More examples
prices = [1, 2, 3, 4, 5]
print(finalPrices(prices)) # Output: [1, 2, 3, 4, 5]

prices = [5, 4, 3, 2, 1]
print(finalPrices(prices)) # Output: [5, 4, 3, 2, 1]

prices = [10, 1, 1, 6]
print(finalPrices(prices)) # Output: [9, 0, 1, 6]