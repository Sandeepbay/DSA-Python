#Creating a Node Class
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

#Creating a Linked List Class with one node
# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
# new_Linked_list = LinkedList(10)
# print(new_Linked_list.length)

#Creating a empty Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Wrting a method to display the linked List
    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

#Inserting a new node at the end of the list
    def append(self,value):
        new_node = Node(value)
        #Checking if the node is empty and Adding a new node in an empty Linked List
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #Adding new node at the end when there are already existing node 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

#Inserting a new node at the beginning of the list
    def prepend(self,value):
        new_node = Node(value)
        #Checking if the node is empty and Adding a new node in an empty Linked List
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #Adding new node at the begining when there is already an existing node 
            new_node.next = self.head
            self.head = new_node
        self.length += 1

#Inserting a node in between the Linked List
    def insert(self,index ,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self , target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self,index):
        current = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            current = current.next
        return current
    
    def set(self , index , value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def PopFirst(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    
    def remove(self , index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.PopFirst()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0
        
new_Linked_list = LinkedList()
new_Linked_list.append(10)
new_Linked_list.append(20)
new_Linked_list.append(30)
new_Linked_list.prepend(5)
new_Linked_list.insert(2,15)
print(new_Linked_list)
#print(new_Linked_list.traverse())
#print(new_Linked_list.search(15))
#print(new_Linked_list.get(2))
#print(new_Linked_list.set(4,50))
#print(new_Linked_list.PopFirst())
#print(new_Linked_list.pop())
#print(new_Linked_list.remove(2))
# print(new_Linked_list.delete_all())
# print(new_Linked_list)