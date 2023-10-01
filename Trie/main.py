# A Trie is a tree based data structure that organizes information in a heiraarchy.
#The different properties are:
# 1. It is typically used to store or search strings in a soace and time efficent way.
# 2. Any Node in trir can store non reptitive multiple characters.
# 3. Every Node stores link of the next character of the string.
# 4. Every Node keeps trac of end of the string. 

#Creation of Trie Node Class
class trieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

#Creation of Trie Node Class
class Trie:
    def __init__(self):
        self.root = trieNode()

    def insertString(self , word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = trieNode()
                current.children.update({ch : node})
            current = node
        current.endOfString = True
        print("Successfully Inserted")

    def searchString(self , word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False

def deleteString(root , index , word):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisBeDeleted = False

    if len(currentNode.children) >= 1:
        deleteString(currentNode , index+1 , word)
        return False
    
    if index == len(word) -1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
        
    if currentNode.endOfString == True:
        deleteString(currentNode , index + 1 , word)
        return False
    
    canThisBeDeleted = deleteString(currentNode , index + 1 , word)
    if canThisBeDeleted == True:
        root.childrn.pop(ch)
        return True
    else:
        return False
        



#All operations carried out
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Apple")
# deleteString(newTrie , 0 , "App")
# print(newTrie.searchString("App"))