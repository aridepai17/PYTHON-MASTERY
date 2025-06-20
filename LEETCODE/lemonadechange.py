# LEETCODE 860

'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''

def lemonadeChange(bills):
    five, ten = 0, 0
    
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

# Example usage
bills1 = [5, 5, 5, 10, 20]
print(lemonadeChange(bills1))  # Output: True

# Additional examples
bills2 = [5, 5, 10]
print(lemonadeChange(bills2))  # Output: True

bills3 = [10, 10]
print(lemonadeChange(bills3))  # Output: False

bills4 = [5, 5, 5, 5, 10, 20]
print(lemonadeChange(bills4))  # Output: True

bills5 = [5, 10, 10]
print(lemonadeChange(bills5))  # Output: False

bills6 = [5, 5, 20]
print(lemonadeChange(bills6))  # Output: True

bills7 = [5, 20, 5, 10]
print(lemonadeChange(bills7))  # Output: False

bills8 = [5, 5, 5, 10, 10, 20]
print(lemonadeChange(bills8))  # Output: False

bills9 = [5, 5, 5, 5, 5, 10, 20]
print(lemonadeChange(bills9))  # Output: True

bills10 = [5, 10, 5, 20]
print(lemonadeChange(bills10))  # Output: True