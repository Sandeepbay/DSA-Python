# A Tree is a non - Linear data structure with heirarchial relationships between its elements without any cycle.
# Tree properties:
# 1. Represent hierarchal data
# 2. Each Node has two components : data and a link to its sub category
# 3. Base Category ans sub categories under it. 

#Tree Terminology - 
#1. Root - Top Node without parent
#2. Edge - A link between parent and child
#3. Leaf - A Node which does not have children
#4. Sibling - Children of same parent
#5. Ancestor - parent , grandparent and great grandparent of a node
#6. Depth of the node - a length of the path from root to the node
#7. Height of the node - a length of the path from the node to the deepest node
#8. Height of the tree - Height of root node
#9. Depth of the tree - Depth of root node

class TreeNode:
    def __init__(self , data , children):
        self.data = data
        self.children = children
    
    def __str__(self , level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self , TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks' , [])
cold = TreeNode('Cold' , [])
hot = TreeNode('Hot' , [])
tree.addChild(cold)
tree.addChild(hot)
cola = TreeNode('Cola' , [])
maaza = TreeNode('Maaza' , [])
tea = TreeNode('Tea' , [])
coffee = TreeNode('Coffee' , [])
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(maaza)
cold.addChild(cola)
print(tree)