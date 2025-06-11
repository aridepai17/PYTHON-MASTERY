# LEETCODE 1773

'''
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. 
You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
1. ruleKey == "type" and ruleValue == typei.
2. ruleKey == "color" and ruleValue == colori.
3. ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
'''

def countMatches(items, ruleKey, ruleValue):
    hashMap = {
        'type' : 0,
        'color' : 1,
        'name' : 2
    }
    count = 0
    for item in items:
        if item[hashMap[ruleKey]] == ruleValue:
            count += 1
    return count

# Example usage:
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
result = countMatches(items, ruleKey, ruleValue)
print(result)  # Output: 1

# Example 
items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
print(countMatches(items1, "type", "phone"))  # Output: 2

# Example 
items2 = [["laptop", "gray", "dell"], ["laptop", "black", "hp"], ["tablet", "gray", "ipad"]]
print(countMatches(items2, "color", "gray"))  # Output: 2

# Example 
items3 = [["car", "red", "honda"], ["bike", "black", "ducati"], ["car", "red", "bmw"]]
print(countMatches(items3, "name", "bmw"))  # Output: 1

# Example 
items4 = [["chair", "brown", "ikea"], ["table", "brown", "walmart"], ["sofa", "blue", "ikea"]]
print(countMatches(items4, "color", "brown"))  # Output: 2