# Stack Operations

# Push method
customStack = []
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
print(customStack)  # Output: [1, 2, 3, 4, 5, 6]


# Pop method
customStack.pop()
print(customStack)  # Output: [1, 2, 3, 4, 5]
customStack.pop()
print(customStack)  # Output: [1, 2, 3, 4]


# Peek method
# To check the top element in the stack without removing it
print(customStack.peek()) # Output: 4


# isEmpty method
# To check if the stack is empty
print(customStack.isEmpty())  # Output: False
customEmptyStack = []
print(customEmptyStack.isEmpty())  # Output: True


# isFull method
# To check if the stack is full (assuming a maximum size)
print(customStack.isFull())  # Output: False

# Assuming a maximum size of 10 for the stack
maxSize = 10
print(len(customStack) == maxSize)  # Output: False


# delete method
# To delete the entire stack
customStack.delete()
print(customStack)  # Output: []




