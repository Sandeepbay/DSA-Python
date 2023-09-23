class TreeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

tree = TreeNode("Drinks") 
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tree.left = leftChild
tree.right = rightChild

# In Pre - order Traversal , We traverse root node first and then we go to the left subtree followed by the right subtree.

def preOrder(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right) 

preOrder(tree)