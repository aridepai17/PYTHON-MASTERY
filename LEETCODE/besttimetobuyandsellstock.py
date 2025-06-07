# LEETCODE 121

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, price - minPrice)
        
    return maxProfit


# Alternate solution without using min() function:

def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            maxProfit = max(maxProfit, price - minPrice)
    return maxProfit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5 (Buy on day 2 at price 1 and sell on day 5 at price 6)

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))  # Output: 0 (No profit can be made)

prices3 = [1, 2, 3, 4, 5]
print(maxProfit(prices3))  # Output: 4 (Buy on day 1 at price 1 and sell on day 5 at price 5)

prices4 = [3, 2, 6, 5, 0, 3]
print(maxProfit(prices4))  # Output: 4 (Buy on day 2 at price 2 and sell on day 3 at price 6)