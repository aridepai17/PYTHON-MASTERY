# CREATING A QUEUE

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

# Time Complexity: O(1)
# Space Complexity: O(1)


# 1. isEmpty() method
# Used to check whether the queue is empty or not

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
# Time Complexity: O(1)
# Space Complexity: O(1)
    
        
# 2. Enqueue() method
# Used to insert element at the end of the queue

    def enqueue(self, value):
        self.items.append(value)
        return
    
# Time Complexity: O(n)
# Space Complexity: O(1)


# 3. Dequeue() method
# Used to delete the first element of the queue

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)
        
# Time Complexity: O(n)
# Space Complexity: O(1)


# 4. Peek() method
# Used to check the first element of the queue

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[0]
        
# Time Complexity: O(1)
# Space Complexity: O(1)