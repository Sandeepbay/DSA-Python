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

# InOrder traversal works in a manner that its gonna traverse left subtree first , then the root node followed by the right subtree.

def InOrder(rootNode):
    if not rootNode:
        return
    InOrder(rootNode.left)
    print(rootNode.data)
    InOrder(rootNode.right)

InOrder(tree)
