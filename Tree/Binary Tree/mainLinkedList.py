import copy as queue

# Creating Node function
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
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
tree.left = leftChild
tree.right = rightChild
leftChild.left = tea
leftChild.right = coffee
rightChild.left = maaza
rightChild.right = cola

# Traversal of binary tree using Pre Order
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)

# preOrder(tree)

# Searching an element in the binary tree
def search(rootNode , nodeValue):
    if not rootNode:
        return "The Binary tree doesnt exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return "Failure"

#print(search(tree , "Tea"))

# Inserting a node in the binary tree

def insert(rootNode , nodeValue):
    if not rootNode:
        rootNode = nodeValue
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            else:
                root.value.left = nodeValue
                return "Successfully inserted in left subtree"
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
            else:
                root.value.right = nodeValue
                return "Successfully inserted in right subtree"

# new = TreeNode("Milk")
# print(insert(tree , new))
# preOrder(tree)

# Deleting a node in the binary tree
# - Getting the deepest node in the binary tree
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)
        deepestNode = root.value
        return deepestNode

# deepestNode = getDeepestNode(tree)
# print(deepestNode.data)

# Function to delete the deepest Node
def deleteDeepestNode(rootNode , dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return
            if root.value.left: 
                if root.value.left == dNode:
                    root.value.left = None
                    return
                else:
                    customQueue.enqueue(root.value.left)
            if root.value.right:
                if root.value.right == dNode:
                    root.value.right = None
                    return
                else:
                    customQueue.enqueue(root.value.right)

# newNode = getDeepestNode(tree)
# deleteDeepestNode(tree , newNode)
# preOrder(tree)

# Deleting a node in the binary tree

def DeleteNode(rootNode , node):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode , dNode)
                return "The Node has been deleted successfully"
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
        return "Node has not been found"
    
# DeleteNode(tree , "Coffee")
# preOrder(tree)

#Deleting an Entire Node
def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "Binary tree has been deleted"

# print(deleteBinaryTree(tree))
# preOrder(tree)



