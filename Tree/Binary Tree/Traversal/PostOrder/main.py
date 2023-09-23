class TreeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

tree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
cola = TreeNode("Cola")
maaza = TreeNode("Maaza")
tree.left  = leftChild
tree.right = rightChild
rightChild.left = cola
rightChild.right = maaza

# Post order Traversal - It first traverse the left subtree then right subtree and then the root Node.

def PostOrder(rootNode):
    if not rootNode:
        return
    PostOrder(rootNode.left)
    PostOrder(rootNode.right)
    print(rootNode.data)

PostOrder(tree)