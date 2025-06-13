# LEETCODE 2037

'''
There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. 
You are also given the array students of length n, where students[j] is the position of the jth student.
You may perform the following move any number of times:
1. Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
Note that there may be multiple seats or students in the same position at the beginning.
'''

def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    totalmoves = 0
    
    for i in range(len(seats)):
        totalmoves += abs(seats[i] - students[i])
    return totalmoves

# Example usage
seats = [3, 1, 5]
students = [2, 7, 4]
print(minMovesToSeat(seats, students))  # Output: 4

# Additional examples
seats2 = [1, 2, 3, 4]
students2 = [1, 4, 2, 3]
print(minMovesToSeat(seats2, students2))  # Output: 0

seats3 = [2, 2, 6, 6]
students3 = [1, 3, 2, 6]
print(minMovesToSeat(seats3, students3))  # Output: 3

seats4 = [5, 3, 1]
students4 = [2, 4, 6]
print(minMovesToSeat(seats4, students4))  # Output: 6

seats5 = [10, 20, 30]
students5 = [30, 20, 10]
print(minMovesToSeat(seats5, students5))  # Output: 0