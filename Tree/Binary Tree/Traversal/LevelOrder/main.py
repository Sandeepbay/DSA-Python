import LinkedListQueue as queue

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

# Level Order Traversal - In Level Order Traversal, It traverses the root node first and then it traverse the second level and next level accordingly , satrting from left to right.

def LevelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)

LevelOrder(tree)
        