#Creating a node

class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class CSLinkedList:
    #Creating a Linked List where there is only one element
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    #Creating a empty Linked List 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result = result + str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result = result + ' -> '
        return result


    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node        
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index > self.length or index < 0:
            return Exception("Index out of range")
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        if self.head == None:
            return None
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break

    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == target:
                return f"Element Found at index {index}"
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            index = index + 1

    def get(self , index):
        if index > self.length or index < 0:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node
    
    def set(self , index , value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def popFirst(self):
        popped_node = self.head
        if self.length == 0:
            return None

        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
        return popped_node.value
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = self.head
            self.tail = temp_node
            popped_node.next = None
            self.length -= 1
        return popped_node.value
    
    def remove(self , index):
        prev_node = self.head
        popped_node = self.get(index)
        if index >= self.length or index < 0 :
            return None
        elif index == 0:
            return self.popFirst()
        elif index == self.length-1:
            return self.pop()
        else:
            for _ in range(index-1):
                prev_node = prev_node.next
                popped_node = prev_node.next
                prev_node.next = popped_node.next
                popped_node.next = None
            self.length -= 1
        return popped_node.value
    
    def delete(self):
        if self.length == 0:
            return None
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
         



cs_Linked_List = CSLinkedList()
cs_Linked_List.append(10)
cs_Linked_List.append(20)
cs_Linked_List.append(30)
cs_Linked_List.append(40)
cs_Linked_List.append(50)
cs_Linked_List.prepend(5)
print(cs_Linked_List)
#cs_Linked_List.get(3)
#print(cs_Linked_List.search(30))
# cs_Linked_List.insert(3,35)
# cs_Linked_List.insert(-1,60)
#print(cs_Linked_List.traverse())
#print(cs_Linked_List.set(3,50))
#print(cs_Linked_List.popFirst())
#print(cs_Linked_List.pop())
#print(cs_Linked_List.remove(5))
#cs_Linked_List.delete()
print(cs_Linked_List)


