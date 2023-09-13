#Creating a node class
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None

#Creating Doubly Linked List Class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Method to print the Linked List
    def print_forward(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.value, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print(" (circular)")

    #Method to print the Linked List backwards
    # def print_backward(self):
    #     if not self.head:
    #         return
    #     current = self.tail
    #     while True:
    #         print(current.value, end=" <-> ")
    #         current = current.prev
    #         if current == self.tail:
    #             break
    #     print(" (circular)")

    #Creating of Doubly Linked List
    def create(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node

    #Method to add Node inside the Linked List
    def addNode(self,value,location):
        new_node = Node(value)
        if self.head is None:
            return None
        #Method to add Node inside the Linked List in the beginning
        elif location == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
            #Method to add Node inside the Linked List in the end
        elif location == 1:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        #Method to add Node inside the Linked List anywhere    
        else:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            new_node.next = temp_node.next.next
            temp_node.next = new_node
            new_node.prev = temp_node
            new_node.next.prev = new_node

    #Method to traverse inside the Linked List
    def traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
    
    #Method to reverse traverse inside the Linked List
    def reverseTraversal(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev
            if temp_node == self.tail:
                break

    #Method to find an element inside the Linked List
    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == target:
                return f"Element has been found at index {index}"
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            index += 1
        return f"Element has not been found"
    
    #Method to delete Node inside the Linked List
    def deleteNode(self,location):
        if self.head == None:
            return None
        #Method to delete Node inside the Linked List in the beginning
        elif location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None  
            else:
                self.head = self.head.next
                self.head.prev = self.tail 
                self.tail.next = self.head
        #Method to delete Node inside the Linked List in tehe end          
        elif location == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        #Method to delete Node inside the Linked List anywhere         
        else:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            temp_node.next = temp_node.next.next
            temp_node.next.prev = temp_node
        print("All Nodes are deleted")

    #Method to delete all the Nodes inside the Linked List
    def DeleteAllNode(self):
        temp_node = self.head
        self.tail.next = None
        while temp_node is not None:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None 

#All operations carried out
CDoublyLL = CircularDoublyLinkedList()
CDoublyLL.create(5)
CDoublyLL.addNode(1,0)
CDoublyLL.addNode(15,1)
CDoublyLL.addNode(10,1)
CDoublyLL.addNode(7,2)
print("Forward:")
CDoublyLL.print_forward()
#CDoublyLL.traversal()
#CDoublyLL.reverseTraversal()
#print(CDoublyLL.search(7))
#CDoublyLL.deleteNode(2)
CDoublyLL.DeleteAllNode()
print("Forward:")
CDoublyLL.print_forward()

# print("Backward:")
# CDoublyLL.print_backward()
