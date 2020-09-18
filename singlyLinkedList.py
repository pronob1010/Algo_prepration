class Node():
    def __init__(self,val):
        self.value = val
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_value(self,val):
        node = Node(val)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_last(self):
        node = self.head
        while node.next is not None:
            previous_node = node
            node = node.next
            #jjkdfhasd
        previous_node.next = None

    def rev_list(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


mylist = SinglyLinkedList()
mylist.add_value(1)
mylist.add_value(2)
mylist.add_value(3)
mylist.add_value(4)

print(mylist)
mylist.remove_last()
print(mylist)
mylist.rev_list()
print(mylist)
mylist.rev_list()
print(mylist)

a, b = list(map(int, input().split()))
print(a + b)
