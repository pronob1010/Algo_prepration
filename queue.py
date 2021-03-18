# Queue using linked list:
# ---------------------------
# class Node():
#     def __init__(self,val):
#         self.prev = None
#         self.value = val
#         self.next = None
#
# class doublylinkedlist():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def push(self, val):
#         node = Node(val)
#         if self.tail is None:
#             self.head = node
#             self.tail = node
#             self.count +=1
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#             self.count +=1
#
#     def pop(self):
#         if self.head is not None:
#             poped_element = self.head.value
#             newfirst = self.head.next
#             self.head = newfirst
#             self.count -=1
#             print("Poped element : ",poped_element)
#
#     def __str__(self):
#         list = []
#         node = self.head
#         while node is not None:
#             list.append(node.value)
#             node = node.next
#         return f"[{', '.join(str(val) for val in list)}]"
#
#
# mylist = doublylinkedlist()
# mylist.push(1)
# mylist.push(3)
# mylist.push(5)
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.push(5)
# print(mylist)
# mylist.push(6)
# print(mylist)
# mylist.pop()
# print(mylist)
# -------------------------------

class Queue:
    def __int__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(13)
q.enqueue(133)
q.enqueue(1322)
q.enqueue(13343)
q.display()
q.dequeue()
q.display()