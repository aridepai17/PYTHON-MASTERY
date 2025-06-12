# Creation of Stack with Limit

from matplotlib.cbook import Stack

class StackWithLimit:
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        return len(self.list) == self.maxSize
    
    def push(self, value):
        if self.isFull():
            return "Stack is full, cannot push value."
        self.list.append(value)
        return self.list
    
    def delete(self):
        self.list = None
        return self.list
    
newStack = Stack(4)
print(newStack.isEmpty())  # Output: True
print(newStack.isFull())   # Output: False
newStack.push(1)
newStack.push(2)
newStack.push(3)
print(newStack)  # Output: [3, 2, 1]
            