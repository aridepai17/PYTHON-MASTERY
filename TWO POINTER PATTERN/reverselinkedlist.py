# LEETCODE 206

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt
        return prev
      
# Example usage
LinkedList = ListNode([1, 2, 3, 4, 5])
head = 1
print(LinkedList.reverseList(head))  # Output: 5 -> 4 -> 3 -> 2 -> 1

# New examples
LinkedList2 = ListNode([10, 20, 30])
head2 = 10
print(LinkedList2.reverseList(head2))  # Output: 30 -> 20 -> 10

LinkedList3 = ListNode([1])
head3 = 1
print(LinkedList3.reverseList(head3))  # Output: 1

LinkedList4 = ListNode([])
head4 = None
print(LinkedList4.reverseList(head4))  # Output: None

LinkedList5 = ListNode([5, 10, 15, 20])
head5 = 5
print(LinkedList5.reverseList(head5))  # Output: 20 -> 15 -> 10 -> 5

LinkedList6 = ListNode([100, 200])
head6 = 100
print(LinkedList6.reverseList(head6))  # Output: 200 -> 100

LinkedList7 = ListNode([1, 2])
head7 = 1
print(LinkedList7.reverseList(head7))  # Output: 2 -> 1

LinkedList8 = ListNode([7, 8, 9, 10, 11])
head8 = 7
print(LinkedList8.reverseList(head8))  # Output: 11 -> 10 -> 9 -> 8 -> 7

LinkedList9 = ListNode([3, 6, 9])
head9 = 3
print(LinkedList9.reverseList(head9))  # Output: 9 -> 6 -> 3

LinkedList10 = ListNode([4])
head10 = 4
print(LinkedList10.reverseList(head10))  # Output: 4