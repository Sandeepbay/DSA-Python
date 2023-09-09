#Middle of a Singly Linked List - Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result        
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        middle_node = self.head
        index = self.length//2
        if self.length % 2 == 0:
            for _ in range(index):
                middle_node = middle_node.next
        else:
            for _ in range(index):
                middle_node = middle_node.next
        return middle_node.value





new_Linked_List = LinkedList()
new_Linked_List.append(10)
new_Linked_List.append(20)
new_Linked_List.append(30)
new_Linked_List.append(40)
new_Linked_List.append(50)
#new_Linked_List.append(60)
print(new_Linked_List)
print(new_Linked_List.find_middle())
print(new_Linked_List)

