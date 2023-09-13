class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
    
    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    # def print_backward(self):
    #     current = self.tail
    #     while current:
    #         print(current.value, end=" <-> ")
    #         current = current.prev
    #     print("None")
    
    def addNode(self,value,position):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            new_node = Node(value)
            if position == 0:
                new_node.next = self.head
                self.head.prev = new_node
                new_node.prev = None
                self.head = new_node
            elif position == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
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

    def traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def reverseTraversal(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev

    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == target:
                return f"Element has been found at index {index}"
            temp_node = temp_node.next
            index += 1
        return "Element has not been found"

    def deleteNode(self,location):
        if self.head is None:
            return "No elements present"
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index +=1
            temp_node.next = temp_node.next.next
            temp_node.next.prev = temp_node
        print("The node has been succesfully deleted")

    def DeleteAllNode(self):
        temp_node = self.head
        while temp_node is not None:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        print("All Nodes has been deleted")


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
