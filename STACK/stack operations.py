# OPERATIONS ON STACKS

# 1. isEmpty()
# Checks if the stack is empty

def isEmpty(self):
    if self.list == []:
        return True
    else:
        return False
    
# Time Complexity: O(1)
# Space Complexity: O(1)


# 2. push()
# Adds an element to the top of the stack

def push(self, value):
    self.list.append(value)
    return self.list

# Time Complexity: O(1)
# Space Complexity: O(1)


# 3. pop()
# Removes the top element from the stack and returns it

def pop(self):
    if isEmpty(self):
        return None
    else:
        return self.list.pop()
    
# Time Complexity: O(1)
# Space Complexity: O(1)


# 4. peek()
# Returns the top element of the stack without removing it

def peek(self):
    if isEmpty(self):
        return None
    else:
        return self.list[-1]
    
# Time Complexity: O(1)
# Space Complexity: O(1)


# 5. delete()
# Deletes the entire stack

def delete(self):
    self.list = []
    return self.list

# Time Complexity: O(1)
# Space Complexity: O(1)