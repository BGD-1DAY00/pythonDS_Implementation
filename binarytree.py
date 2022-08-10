
class Node: 
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node =  None
        self.parent_node = parent
        
# When Working with recursion think about how the stack is being populated
class BinarySearchTree: 
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        node = Node(data, None)
        if(self.root is None):
            self.root = node
        else:
            self.insertNode(data, self.root)
            
    def insertNode(self, data, root):
        if data < root.data: 
            if root.left_node is not None:
                self.insertNode(data, root.left_node)
            else: 
                root.left_node = Node(data, root)
        else: 
            if root.right_node is not None:
                self.insertNode(data, root.right_node)
            else: 
                root.right_node = Node(data, root.right_node)
                
# min max run in logarithmic time
    def getMin(self):
        if self.root is None:
            return;
        if self.root:
            return self.get_min_value(self.root)
        
    def get_min_value(self, root):
        if root.left_node:
            return self.get_min_value(root.left_node)
        else: 
            print(root.data)
            return root.data
        
    def getMax(self):
        if self.root is None:
            return;
        if self.root:
            return self.get_max_value(self.root)
        
    def get_max_value(self, root):
        if root.right_node:
            return self.get_max_value(root.right_node)
        else: 
            print(root.data)
            return root.data
        
        
    # inorder traversal runs in log time
    def inorder_travese(self):
        return self.inorder(self.root)
    
    def inorder(self, node):
        if node.left_node:
            self.inorder(node.left_node)
        print(node.data)
        if node.right_node:
            self.inorder(node.right_node)

    def remove(self, val):
        target = Node(val)
        self.searc(self.root, target)
    
    def search(self, root, target):
        if target.data < root.data:
            if root.left_node is not None:
                self.search(root.left_node, target)
        elif target.data > root.data:
            if root.right_node is not None:
                self.search(root.right_node, target)
        else:
            # if it has no children
            if root.left_node is None and root.right_node is None:
                
            if root.left_node is None or root.right_node is None:
                if root.left_node is None:
                    root.parent.left_node = 
            # one child
            # two children
            
            
        
    
        
           

bst = BinarySearchTree()
bst.insert(1)
bst.insert(433)
bst.insert(23)
bst.inorder_travese()

bst.getMin()
bst.getMax()