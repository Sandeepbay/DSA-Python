# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next

#     def create(self,value):
#         node = Node(value)
#         node.next = None
#         node.prev = None
#         self.head = node
#         self.tail = node
#         print(node)
#         return "New Node has been created"

# new_Double_Linked_List = DoubleLinkedList()
# print(new_Double_Linked_List.create(5))
# print(node.value for node in new_Double_Linked_List)
