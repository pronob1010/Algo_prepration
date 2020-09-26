# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class singlyLinkedList():
#     def __init__(self):
#         self.head = None
#
#     def addNode(self, x):
#         node = ListNode(x)
#
#         start = self.head
#         if start is None:
#             start = node
#         else:
#             start.next = node
#
#     def deleteNode(self, node):
#         # node.val = node.next.val
#         # node.next = node.next.next
#         start = self.head
#
#         if start.val == node.val:
#             self.head = start.next
#         else:
#             while(start.next is not None):
#                 if (node.val == start.val):
#                     previous = node.next
#                 previous = start.next
#                 start = start.next
#
#
#     def display(self):
#         start = self.head
#         while start is not None:
#             print(start.val)
#             start = start.next
#
#
# mylist = singlyLinkedList()
# mylist.addNode(1)
# mylist.addNode(2)
# mylist.addNode(3)
# mylist.addNode(4)
# mylist.addNode(5)
# mylist.display()


class Node():
    def __init__(self, value):
        self.next = None
        self.val = value
        self.position = 0


class singlyLinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, value):
        node = Node(value)
        # start = self.head

        if self.head is None:
            self.head = node
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = node
            # self.head.next = node
        # self.position += 1

    def insertIntoHeadNode(self, value):
        node = Node(value)
        previousNode = self.head
        self.head = node
        node.next = previousNode
        # self.position += 1

    def insertByPosition(self, value, pos):
        node = Node(value)
        current = self.head
        position = 1
        pos = pos
        if (pos==1):
            self.insertIntoHeadNode(value)
        else:
            while(pos != position):
                prev = current
                position +=1
                current = current.next
            prev.next = node
            node.next = current
        # node.next = prev.next.next
        #problem acheeeeeeeeeeeeeeeeeeeeeeeeee


    def display(self):
        start = self.head
        while start is not None:
            print(start.val, end=" ")
            start = start.next


mylist = singlyLinkedList()
mylist.addNode(1)
mylist.addNode(2)
mylist.addNode(3)
mylist.addNode(4)
mylist.addNode(5)
mylist.insertIntoHeadNode(6)
mylist.display()
print("--")
mylist.insertByPosition(7, 1)
mylist.display()
