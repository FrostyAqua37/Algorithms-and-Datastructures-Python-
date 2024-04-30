#Programming Task 3.
class TreeNode:

    def __init__(self, value):
        #Initialization of the nodes.
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        #Function to insert value left or right depending on the value of the node
        if value < self.value:
            #Inserts value to the left side if its less than the root node
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else: 
            #Inserts value to the right side if its equal or greater than the root node
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        #Recursive function to traverse the binary search tree.
        if self.left:
            #Traverse to the last left side node first and starts printing out the values.
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
             #Traverse to the last right side node first and starts printing out the values.
            self.right.inorder_traversal()

binarySearchTree = TreeNode(21)
binarySearchTree.insert(14)
binarySearchTree.insert(11)
binarySearchTree.insert(18)
binarySearchTree.insert(15)
binarySearchTree.insert(19)
binarySearchTree.insert(28)
binarySearchTree.insert(25)
binarySearchTree.insert(32)
binarySearchTree.insert(30)

binarySearchTree.inorder_traversal()
