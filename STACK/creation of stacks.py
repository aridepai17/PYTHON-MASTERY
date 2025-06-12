# CREATION OF STACKS

# 1. STACK USING LIST
# Easy ot implement
# Speed problem when it grows


# 2. STACK USING LINKED LIST
# Fast performance
# Implementation is complex


# Creation of Stack using Python List

class Stack:
    def __init_(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [ str(x) for x in self.list ]
        return '\n'.join(values)
    
# Time Complexity: O(1)
# Space Complexity: O(1)


# String representation of Stack

class Stack:
    def __init__(self):
        self.list = []
        
def __str__(self):
    values = [ str(x) for x in reversed(self.list) ]
    return '\n'.join(values)


# Creation of Stack using Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0


# Operations on Stack using Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next
        
class Stack:
    def __init__(self):
        self.LinkedListStack = LinkedListStack()
        
        
# 1. isEmpty()
    def isEmpty(self):
        if self.LinkedListStack.head == None:
            return True
        else:
            return False

# Time Complexity: O(1)
# Space Complexity: O(1)


# 2. push()
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedListStack.head
        self.LinkedListStack.head = node
        
# Time Complexity: O(1)
# Space Complexity: O(1)


# 3. pop()
    def pop(self):
        if self.isEmpty():
            return None
        else:
            poppedNode = self.LinkedListStack.head.value
            self.LinkedListStack.head = self.LinkedListStack.head.next
            return poppedNode
        
# Time Complexity: O(1)
# Space Complexity: O(1)


# 4. peek()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.LinkedListStack.head.value
        
# Time Complexity: O(1)
# Space Complexity: O(1)


# 5. delete()
    def delete(self):
        self.LinkedListStack.head = None
        
# Time Complexity: O(1)
# Space Complexity: O(1)