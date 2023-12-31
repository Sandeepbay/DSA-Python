# Binary Heap - A Binary heap is a part of binary tree that is a Binary Heap also has at most two children. 
# There are two types of binary heap - 1. Max Heap 2. Min Heap. In a Min Heap , the value of each Node should be minimum when compared to the children of the nodes and the same goes for the Max Heap where the value of eaach Node should be the maximum.
# Another property of Heap is the tree should be complete. It should have all the nodes filled except the last level. If the nodes in the last level is not filled, then the nodes should be filled complete left of the tree.

# Creating Heap class
class Heap:
    def __init__(self , size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# A Method to return the rootNode of the Bianry Heap
def peakOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
# A Method to return the size of the Bianry Heap
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

# A Method to traverse in Level Order
def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1 , rootNode.heapSize + 1):
            print(rootNode.customList[i])

# A Method to balance the Bianry Heap
def heapifyTreeInsert(rootNode , index , heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode , parentIndex , heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode , parentIndex , heapType)

# A Method to insert element in the Bianry Heap
def insertNode(rootNode , nodeValue , heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Tree is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode , rootNode.heapSize , heapType)
    return "The value has been inserted"

#Helper function
def heapifyTreeExtract(rootNode , index , heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp =  rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp =  rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp =  rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp =  rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode , swapChild , heapType)


# A Method to delete element in the Bianry Heap
def extractNode(rootNode , heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode , 1 , heapType)
        return extractedNode

# A Method to delete the Bianry Heap
def deleteBinaryTree(rootNode):
    rootNode.customList = None

#All operations carried out  
newHeapTree = Heap(5)
#print(newHeapTree.customList)
#print(peakOfHeap(newHeapTree))
#print(sizeOfHeap(newHeapTree))
insertNode(newHeapTree , 4 , "Max")
insertNode(newHeapTree , 5 , "Max")
insertNode(newHeapTree , 3 , "Max")
insertNode(newHeapTree , 2 , "Max")
insertNode(newHeapTree , 1 , "Max")
#print(extractNode(newHeapTree , "Max"))
#fdeleteBinaryTree(newHeapTree)
levelOrder(newHeapTree)
