# Creating a Binary Tree Class
class BinaryTree:
    def __init__(self , size):
        self.customList = size * [None]
        self.LastUsedIndex = 0
        self.maxSize = size

    # A method to add values 
    def insertNode(self, value):
        if [self.LastUsedIndex + 1] == self.maxSize:
            return "The List is full"
        else:
            self.customList[self.LastUsedIndex + 1] = value
            self.LastUsedIndex += 1
            return "Value has been inserted"

    #A method to search inside the Tree
    def searchNode(self , nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

    # A method to traverse in preOrder
    def preOrder(self , index):
        if index > self.LastUsedIndex:
            return
        print(self.customList[index])
        self.preOrder(index * 2)
        self.preOrder(index * 2 + 1)

    # A method to traverse in inOrder
    def inOrder(self , index):
        if index > self.LastUsedIndex:
            return
        self.inOrder(index * 2)
        print(self.customList[index])
        self.inOrder(index * 2 + 1)

    # A method to traverse in postOrder
    def postOrder(self , index):
        if index > self.LastUsedIndex:
            return
        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customList[index])

    # A method to traverse in levelOrder
    def levelOrder(self , index):
        for i in range(index , len(self.customList)):
            if self.customList[i] == None:
                continue
            print(self.customList[i])

    # A method to delete a node
    def deleteNode(self , node):
        if self.LastUsedIndex == 0:
            return "No node inside the List"
        for i in range(1 , self.LastUsedIndex + 1):
            if self.customList[i] == node:
                self.customList[i] = self.customList[self.LastUsedIndex]
                self.customList[self.LastUsedIndex] = None
                self.LastUsedIndex -= 1
        return "Deleted Successfully"
    
    # A method to delete an entire tree
    def deleteBinaryTree(self):
        self.customList = None
            
        
# All Operations carried out
tree = BinaryTree(8)
print(tree.insertNode("Drinks"))
print(tree.insertNode("Hot"))
print(tree.insertNode("Cold"))
#print(tree.searchNode("Hot"))
print(tree.insertNode("Tea"))
print(tree.insertNode("Coffee"))
#tree.preOrder(1)
#tree.inOrder(1)
#tree.postOrder(1)
#print(tree.deleteNode("Drinks"))
tree.deleteBinaryTree()
tree.levelOrder(1)