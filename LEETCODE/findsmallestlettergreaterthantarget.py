# LEETCODE 744

'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.
'''

def nextGreatestLetter(letters, target):
  left, right = 0, len(letters) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if letters[mid] <= target:
      left = mid + 1
    else:
      right = mid - 1
      
    return letters[left % len(letters)]
  
# Example usage:
letters = ['a', 'b', 'c', 'd', 'e', 'f']
target = 'c'
print(nextGreatestLetter(letters, target))  # Output: 'd'

# Additional examples:
letters1 = ['a', 'b', 'c', 'd', 'e', 'f']
target1 = 'f'
print(nextGreatestLetter(letters1, target1))  # Output: 'a'

letters2 = ['x', 'y', 'z']
target2 = 'y'
print(nextGreatestLetter(letters2, target2))  # Output: 'z'

letters3 = ['m', 'n', 'o', 'p']
target3 = 'm'
print(nextGreatestLetter(letters3, target3))  # Output: 'n'

letters4 = ['a', 'c', 'e', 'g']
target4 = 'b'
print(nextGreatestLetter(letters4, target4))  # Output: 'c'

letters5 = ['a', 'b', 'c', 'd']
target5 = 'a'
print(nextGreatestLetter(letters5, target5))  # Output: 'b'

letters6 = ['a', 'b', 'c', 'd', 'e']
target6 = 'e'
print(nextGreatestLetter(letters6, target6))  # Output: 'a'

letters7 = ['g', 'h', 'i', 'j']
target7 = 'g'
print(nextGreatestLetter(letters7, target7))  # Output: 'h'

letters8 = ['p', 'q', 'r', 's']
target8 = 'r'
print(nextGreatestLetter(letters8, target8))  # Output: 's'

letters9 = ['a', 'b', 'c', 'd', 'e', 'f']
target9 = 'z'
print(nextGreatestLetter(letters9, target9))  # Output: 'a'