# Node constructor

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
new_node = Node(10)
print(new_node)

# Creation of Singly Linked List

# 1. Linked List that has a single element


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    newNode = Node(value)
    self.head = newNode
    self.tail = newNode
    self.length = 1
    
LinkedList1 = LinkedList(10)
print(LinkedList1) # Output: <__main__.LinkedList object at 0x...>
print(LinkedList1.head.value) # Output: 10
print(LinkedList1.tail.value) # Output: 10

# 2. Linked List that has no elements

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
LinkedList2 = LinkedList()
print(LinkedList2) # Output: <__main__.LinkedList object at 0x...>
print(LinkedList2.head) # Output: None
print(LinkedList2.tail) # Output: None