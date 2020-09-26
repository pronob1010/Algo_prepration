# class Node():
#     def __init__(self,val):
#         self.value = val
#         self.next = None
#
# class SinglyLinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_value(self,val):
#         node = Node(val)
#
#         if self.tail is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def remove_last(self):
#         node = self.head
#         while node.next is not None:
#             previous_node = node
#             node = node.next
#             #jjkdfhasd
#         previous_node.next = None
#
#     def rev_list(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev
#
#
#
#     def __str__(self):
#         vals=[]
#         node = self.head
#         while node is not None:
#             vals.append(node.value)
#             node = node.next
#         return f"[{', '.join(str(val) for val in vals)}]"
#
#
# mylist = SinglyLinkedList()
# mylist.add_value(1)
# mylist.add_value(2)
# mylist.add_value(3)
# mylist.add_value(4)
#
# print(mylist)
# mylist.remove_last()
# print(mylist)
# mylist.rev_list()
# print(mylist)
# mylist.rev_list()
# print(mylist)
#
# a, b = list(map(int, input().split()))
# print(a + b)


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
        #problem solved

    def delLastNode(self):
        current = self.head

        while(current.next is not None):
            previous = current
            current = current.next
        previous.next = None
        del(current)

    def deletefirstNode(self):
        head = self.head
        self.head = head.next
        del(head)

    def deleteByPosition(self,pos):
        current = self.head
        position  = 0
        previous = current
        while current is not None:
            if position == pos:
                previous.next = current.next
                del(current)
                break
            position+=1
            previous = current
            current = current.next


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

print("\nInsert by Position")
mylist.insertByPosition(7, 1)
mylist.display()

print("\nDelete last Node :")
mylist.delLastNode()
mylist.display()

print("\nDelete First Node :")
mylist.deletefirstNode()
mylist.display()

print("\nDelete by Position")
mylist.deleteByPosition(2)
mylist.display()
