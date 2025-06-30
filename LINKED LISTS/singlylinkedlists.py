# Node constructor

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
new_node = Node(10)
print(new_node) # Output: <__main__.Node object at 0x...>

# Creation of Singly Linked List

# 1. Singly Linked List that has a single element


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

# 2. Singly Linked List that has no elements

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
LinkedList2 = LinkedList()
print(LinkedList2) # Output: <__main__.LinkedList object at 0x...>
print(LinkedList2.head) # Output: None
print(LinkedList2.tail) # Output: None

# Inserting element at the end of the Singly Linked List

class LinkedList:
  def __init__(self, value):
    self.head = None
    self.tail = None
    self.length = 0
    
  def append(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1
    
  def __str__(self): # Printing the Linked List
    tempNode = self.head
    result = ''
    while tempNode is not None:
      result += str(tempNode.value)
      if tempNode.next is not None:
        result += ' -> '
      tempNode = tempNode.next
    return result
    
LinkedList3 = LinkedList()
LinkedList3.append(10)
LinkedList3.append(20)
print(LinkedList3.head.value)  # Output: 10
print(LinkedList3.tail.value)  # Output: 20
print(LinkedList3.length)  # Output: 2
print(LinkedList3) # Output: 10 -> 20

# Time Complexity: O(1) for appending at the end
# Space Complexity: O(1) for appending at the end


# Inserting element at the beginning of the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def prepend(self, value): # Inserting at the beginning
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1
    
LinkedList4 = LinkedList()
LinkedList4.prepend(10)
LinkedList4.prepend(20)
LinkedList4.prepend(30)
print(LinkedList4.head.value)  # Output: 30
print(LinkedList4.tail.value)  # Output: 10
print(LinkedList4.length)  # Output: 3
print(LinkedList4) # Output: 30 -> 20 -> 10

# Time Complexity: O(1) for prepending at the beginning
# Space Complexity: O(1) for prepending at the beginning


# Inserting element at a specific index in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def insert(self, index, value): # Inserting at a specific index
    newNode = Node(value)
    if index < 0 or index > self.length:
      return False
    elif self.length == 0:
      self.head = newNode
      self.tail = newNode
    elif index == 0:
      newNode.next = self.head
      self.head = newNode
    else:
      tempNode = self.head
      for _ in range(index - 1):
        tempNode = tempNode.next
      newNode.next = tempNode.next
      tempNode.next = newNode
    self.length += 1
    return True
    
LinkedList5 = LinkedList()
LinkedList5.insert(0, 10)  # Insert at the beginning
LinkedList5.insert(1, 20)  # Insert at the end
print(LinkedList5.head.value)  # Output: 10
print(LinkedList5.tail.value)  # Output: 20
print(LinkedList5.length)  # Output: 2
print(LinkedList5) # Output: 10 -> 20

# Time Complexity: O(n) for inserting at a specific index
# Space Complexity: O(1) for inserting at a specific index
      
      
# Traversing the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

def traverseLinkedList(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next
      
LinkedList6 = LinkedList()
LinkedList6.append(10)
LinkedList6.append(20)
LinkedList6.append(30)
LinkedList6.traverseLinkedList() # Output: 10 20 30

# Time Complexity: O(n) for traversing the linked list
# Space Complexity: O(1) for traversing the linked list


# Searching for an element in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def searchElement(self, target): # Searching for an element, return True or False
    current = self.head
    while current:
      if current.value == target:
        return True
      current = current.next
    return False
  
  def searchElementreturnIndex(self, target): # Searching for an element, returns index or -1 if not found
    current = self.head
    index = 0
    while current:
      if current.value == target:
        return index
      current = current.next
      index += 1
    return -1
  
LinkedList7 = LinkedList()
LinkedList7.append(10)
LinkedList7.append(20)
LinkedList7.append(30)
LinkedList7.append(40)
LinkedList7.append(50)
print(LinkedList7.searchElement(30))  # Output: True
print(LinkedList7.searchElement(60))  # Output: False
print(LinkedList7.searchElementreturnIndex(30))  # Output: 2
print(LinkedList7.searchElementreturnIndex(60))  # Output: -1

# Time Complexity: O(n) for searching for an element
# Space Complexity: O(1) for searching for an element


# Get method in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def get(self, index):  # Get the value at a specific index
    if index == -1:
      return self.tail.value
    if index < -1 or index >= self.length:
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current.value
  
LinkedList8 = LinkedList()
LinkedList8.append(10)
LinkedList8.append(20)
LinkedList8.append(30)
print(LinkedList8.get(0))  # Output: 10
print(LinkedList8.get(1))  # Output: 20
print(LinkedList8.get(2))  # Output: 30
print(LinkedList8.get(-1))  # Output: 30
print(LinkedList8.get(3))  # Output: None

# Time Complexity: O(n) for getting the value at a specific index
# Space Complexity: O(1) for getting the value at a specific index


# Set Method in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def set(self, index, value):  # Set the value at a specific index
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
  
LinkedList9 = LinkedList()
LinkedList9.append(10)
LinkedList9.append(20)
LinkedList9.append(30)
print(LinkedList9.set(1, 25))  # Output: True
print(LinkedList9.set(3, 40))  # Output: False
print(LinkedList9.set(2, 35))  # Output: True
print(LinkedList9) # Output: 10 -> 25 -> 35

# Time Complexity: O(n) for setting the value at a specific index
# Space Complexity: O(1) for setting the value at a specific index


# Pop First Method in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def popFirst(self):  # Remove the first element
    if self.length == 0:
      return None
    poppedNode = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      poppedNode.next = None
    self.length -= 1
    return poppedNode.value
  
LinkedList10 = LinkedList()
LinkedList10.append(10)
LinkedList10.append(20)
LinkedList10.append(30)
LinkedList10.append(40)
print(LinkedList10.popFirst())  # Output: 10
print(LinkedList10.popFirst())  # Output: 20
print(LinkedList10) # Output: 30 -> 40

# Time Complexity: O(1) for popping the first element
# Space Complexity: O(1) for popping the first element


# Pop Method in the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def pop(self):  # Remove the last element
    if self.length == 0:
      return None
    poppedNode = self.tail
    if self.length == 1:
      self.head = self.tail = None
    else:
      temp = self.head
      while temp.next is not self.tail:
        temp = temp.next
      self.tail = temp
      temp.next = None
    self.length -= 1
    return poppedNode.value
  
LinkedList11 = LinkedList()
LinkedList11.append(10)
LinkedList11.append(20)
LinkedList11.append(30)
LinkedList11.append(40)
print(LinkedList11.pop())  # Output: 40
print(LinkedList11.pop())  # Output: 30
print(LinkedList11) # Output: 10 -> 20

# Time Complexity: O(n) for popping the last element
# Space Complexity: O(1) for popping the last element


# Remove method on the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def remove(self, index):  # Remove an element at a specific index
    if index < -1 or index >= self.length:
      return None
    if index == 0:
      return self.popFirst()
    if index == self.length - 1 or index == -1:
      return self.pop()
    prevNode = self.get(index - 1)
    poppedNode = prevNode.next
    prevNode.next = poppedNode.next
    poppedNode.next = None
    self.length -= 1
    return poppedNode.value
  
LinkedList12 = LinkedList()
LinkedList12.append(10)
LinkedList12.append(20)
LinkedList12.append(30)
LinkedList12.append(40)
print(LinkedList12.remove(1))  # Output: 20
print(LinkedList12.remove(2))  # Output: 30
print(LinkedList12) # Output: 10 -> 40

# Time Complexity: O(n) for removing an element at a specific index
# Space Complexity: O(1) for removing an element at a specific index
    
    
# Deleting all elements from the Singly Linked List

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def deleteAll(self):  # Delete all elements
    self.head = None
    self.tail = None
    self.length = 0
    return None
    
LinkedList13 = LinkedList()
LinkedList13.append(10)
LinkedList13.append(20)
LinkedList13.append(30)
print(LinkedList13.length)  # Output: 3
print(LinkedList13.deleteAll())  # Output: None
print(LinkedList13) 

# Time Complexity: O(1) for deleting all elements
# Space Complexity: O(1) for deleting all elements