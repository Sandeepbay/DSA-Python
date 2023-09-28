import path as queue

# Creating AVL Node class
class AVLNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

#Pre - order Traversal
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)

#In-Order traversal
def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)

#Post-Order Traversal
def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)

#Level Order Traversal
def levelOrder(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.left is not None:
            customQueue.enqueue(root.value.left)
        if root.value.right is not None:
            customQueue.enqueue(root.value.right)

# Search Operation
def search(rootNode , nodeValue):
    if rootNode.data == nodeValue:
        return "Element has been found"
    elif nodeValue < rootNode.data:
        if rootNode.left.data == nodeValue:
            return "Element has been found"
        else:
            search(rootNode.left , nodeValue)
    else:
        if rootNode.right.data == nodeValue:
            return "Element has been found"
        else:
            search(rootNode.right , nodeValue)


#All operations carried out
newAVL = AVLNode(10)
preOrder(newAVL)
inOrder(newAVL)
postOrder(newAVL)
levelOrder(newAVL)
print(search(newAVL , 10))