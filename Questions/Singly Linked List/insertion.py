#Insertion at the Beginning of a Singly Linked List - Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = None
        self.length = 0
        
    def prepend(self , value):
        new_node = Node(value)
        self.head = new_node
        self.length += 1

new_linked_list = LinkedList(10)
new_linked_list.prepend(20)
print(new_linked_list.head.value)