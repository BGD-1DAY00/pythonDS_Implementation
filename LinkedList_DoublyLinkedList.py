
class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
        self.previous = None

class  LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            
    def traverseForward(self):
        if(self.head == None):
            return
        pointer = self.head
        while pointer != None:
            print(pointer.data)
            pointer = pointer.next
            
                
    def traverseBackward(self):
        if(self.tail ==None):
            return
        pointer = self.tail
        while pointer != None:
            print(pointer.data)
            pointer = pointer.previous
            
linkedList = LinkedList();
linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(3)

linkedList.traverseBackward()
print('---------')
linkedList.traverseForward()
            
            
# Singly Linked List Implementation

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while pointer !=None:
                pointer = pointer.next
            pointer.next = node
            
    def insertAtStart(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def removeNode(self, val):
        if self.head is None: 
            return
        # if the size of the linked list is 1 
            
        curr = self.head
        previousPointer = None
        while curr.data != val:
            previousPointer = curr
            curr = curr.next
        previousPointer.next = curr.next
        curr.next = None
        
    def size(self):
        length = 0
        curr = self.head
        while curr != None:
            length +=1
            curr = curr.next
        return length
      