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

#Helper Functions for inserting - 
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rotateRight(disbalancedNode):
    newRoot = disbalancedNode.left
    disbalancedNode.left = disbalancedNode.left.right
    newRoot.right = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left) , getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left) , getHeight(newRoot.right))
    return newRoot

def rotateLeft(disbalancedNode):
    newRoot = disbalancedNode.right
    disbalancedNode.right = disbalancedNode.right.left
    newRoot.left = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left) , getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left) , getHeight(newRoot.right))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)

#Insertion Operation
def insertNode(rootNode , nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left , nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right , nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.left) , getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.left.data:
        return rotateRight(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = rotateLeft(rootNode.left)
        return rotateRight(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data:
        return rotateLeft(rootNode)
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rotateRight(rootNode.right)
        return rotateLeft(rootNode)
    return rootNode

#Helper function for deleting - 
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValueNode(rootNode.left)

#Deleting Operation
def deleteNode(rootNode , nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left , nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right , nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right , temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.left) , getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.left) >= 0:
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.right) <= 0:
        return rotateLeft(rootNode)
    if balance > 1 and getBalance(rootNode.left) < 0:
        rootNode.left = rotateLeft(rootNode.left)
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.right) > 0:
        rootNode.right = rotateRight(rootNode.right)
        return rotateLeft(rootNode)
    return rootNode

# Deleting Entire AVL Tree

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.left =  None
    rootNode.right = None
    return "AVL Tree has been deleted"
    

#All operations carried out
newAVL = AVLNode(10)
# preOrder(newAVL)
# inOrder(newAVL)
# postOrder(newAVL)
# print(search(newAVL , 10))
newAVL = insertNode(newAVL , 20)
newAVL = insertNode(newAVL , 30)
newAVL = insertNode(newAVL , 40)
#newAVL = deleteNode(newAVL , 20)
#print(deleteAVL(newAVL))
levelOrder(newAVL)