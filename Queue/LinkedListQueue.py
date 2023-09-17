#Creating Node Class
class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

#Creating LinkedList Class    
class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        temp_node = self.head
        while temp_node is not None:
            yield temp_node
            temp_node = temp_node.next

#Creating Queue Class
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    #A method to add elements in the Queue
    def enqueue(self,value):
        new_node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    #A method to check if Queue is empty or not
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    #A method to remove the first element in the Queue    
    def dequeue(self):
        if self.isEmpty():
            return "No elements present in the Queue"
        else:
            popped_node = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = self.linkedList.tail = None
            else:
                self.linkedList.head = popped_node.next
            return popped_node

    #A method to return the first element in the Queue    
    def peek(self):
        if self.isEmpty():
            return "No elements present in the Queue"
        else:
            peekNode = self.linkedList.head
            return peekNode

    #A method to delete the entire Queue   
    def deleteQueue(self):
        self.linkedList.head = self.linkedList.tail = None
            
#Operations carried out
new_Queue = Queue()
new_Queue.enqueue(3)
new_Queue.enqueue(6)
new_Queue.enqueue(9)
new_Queue.enqueue(12)
new_Queue.enqueue(15)
#print(new_Queue.isEmpty())
print(new_Queue)
# print(new_Queue.peek())
# print(new_Queue.dequeue())
# print(new_Queue)
# new_Queue.deleteQueue()
# print(new_Queue)


