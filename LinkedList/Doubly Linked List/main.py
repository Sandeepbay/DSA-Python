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

DoublyLL = DoublyLinkedList()
DoublyLL.create(5)
DoublyLL.addNode(0,0)
DoublyLL.addNode(10,1)
DoublyLL.addNode(7.5,2)
#DoublyLL.traversal()
#DoublyLL.reverseTraversal()

print("Forward:")
DoublyLL.print_forward()

# print("Backward:")
# DoublyLL.print_backward()
