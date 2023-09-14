#Creating node for Stack Linked List
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

#Creating a Linked List for the Stack
class LinkedList:
    def __init__(self):
        self.head = None

    #A Method to iterate through the Stack
    def __iter__(self):
        currentNode = self.head
        while currentNode is not None:
            yield currentNode
            currentNode = currentNode.next

#A Class to create Stack
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    #A Method to display the Stack
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    #A method to check if the stack is empty or not
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    #A Method to add elements inside the stack      
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node

    #A method to remove element from the stack
    def pop(self):
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue
    
    #A method to check the first element in the stack i.e last element pushed inside the stack
    def peek(self):
        nodeValue = self.LinkedList.head.value
        return nodeValue
    
    #A method to delete the entire Stack
    def deleteStack(self):
        self.head = None


#All operations carried out    
new_Stack = Stack()
#print(new_Stack.isEmpty())
new_Stack.push(1)
new_Stack.push(2)
new_Stack.push(3)
new_Stack.push(4)
new_Stack.push(5)
#print(new_Stack.pop())
#print(new_Stack.peek())
#new_Stack.deleteStack()
print("--------")
print(new_Stack)
