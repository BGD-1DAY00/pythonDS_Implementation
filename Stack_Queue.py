
# Doubly Linked List Implementation
# from time import sleep
# i = [1,2,3,4]
# i.insert(i, 5)
# print(i)
       


 # Stack  

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def insert(self, val):
        self.stack.append = val
        
    def pop(self,val):
        if len(self.stack) < 1:
            return None
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
        

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    
    def insert(self,val):
        self.queue.insert(0, val)
        
    def pop(self,val):
        if len(self.queue) ==0:
            return "emptey Queue"

        data = self.queue[0]
        self.queue.pop(0)
        return data
    
    def size(self, val):
        return len(self.queue)
        
        
        
                
            