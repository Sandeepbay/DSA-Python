#Creating a node class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

#Creating Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Method to iterate over the Linked List
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    #Creating of Doubly Linked List
    def create(self,value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "The node has been created succesfully"
    
    #Method to print the Linked List
    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    #Method to print the Linked List backwards
    # def print_backward(self):
    #     current = self.tail
    #     while current:
    #         print(current.value, end=" <-> ")
    #         current = current.prev
    #     print("None")
    
    #Method to add Node inside the Linked List
    def addNode(self,value,position):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            new_node = Node(value)
            #Method to add Node inside the Linked List in the beginning
            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                new_node.prev = None
                self.head = new_node
            #Method to add Node inside the Linked List in the end
            elif position == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            #Method to add Node inside the Linked List anywhere
            else:
                temp_node = self.head
                index = 0
                while index < position - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    #Method to traverse inside the Linked List
    def traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    #Method to reverse traverse inside the Linked List
    def reverseTraversal(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev

    #Method to find an element inside the Linked List
    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == target:
                return f"Element has been found at index {index}"
            temp_node = temp_node.next
            index += 1
        return "Element has not been found"

    #Method to delete Node inside the Linked List
    def deleteNode(self,location):
        if self.head is None:
            return "No elements present"
        #Method to delete Node inside the Linked List in the beginning
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        #Method to delete Node inside the Linked List in tehe end
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        #Method to delete Node inside the Linked List anywhere        
        else:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index +=1
            temp_node.next = temp_node.next.next
            temp_node.next.prev = temp_node
        print("The node has been succesfully deleted")

    #Method to delete all the Nodes inside the Linked List
    def DeleteAllNode(self):
        temp_node = self.head
        while temp_node is not None:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        print("All Nodes has been deleted")

#All operations carried out
DoublyLL = DoublyLinkedList()
DoublyLL.create(5)
DoublyLL.addNode(0,0)
DoublyLL.addNode(10,1)
DoublyLL.addNode(7.5,2)
print("Forward:")
DoublyLL.print_forward()
#DoublyLL.DeleteAllNode()
#DoublyLL.print_forward()
#DoublyLL.traversal()
#DoublyLL.reverseTraversal()
#print(DoublyLL.search(7.5))
#DoublyLL.deleteNode(2)

# print("Backward:")
# DoublyLL.print_backward()
