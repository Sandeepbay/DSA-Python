import copy as queue

#Creating Binary Search Tree class
class binarySearchTree:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

# Inserting a node in the Binary Search Tree
def insertNode(rootNode , nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = binarySearchTree(nodeValue)
        else:
            insertNode(rootNode.left , nodeValue)
    elif nodeValue >= rootNode.data:
        if rootNode.right is None:
            rootNode.right = binarySearchTree(nodeValue)
        else:
            insertNode(rootNode.right , nodeValue)
    return "Node has been inserted"

# A method to traverse in preOrder
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)

# A method to traverse in inOrder
def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)

# A method to traverse in postOrder
def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)

# A method to traverse in levelOrder
def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
#Checking

#All Operations carried out
newTree = binarySearchTree(None)
insertNode(newTree , 70)
insertNode(newTree , 55)
insertNode(newTree , 95)
insertNode(newTree , 40)
insertNode(newTree , 20)
insertNode(newTree , 65)
insertNode(newTree , 69)
insertNode(newTree , 90)
insertNode(newTree , 105)
insertNode(newTree , 93)
# print(newTree.data)
# print(newTree.left.data)
# print(newTree.right.data)
# preOrder(newTree)
# inOrder(newTree)
# postOrder(newTree)
#levelOrder(newTree)
