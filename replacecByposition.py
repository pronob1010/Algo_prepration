class Node():
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None

class dublyLinkedList():
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def add(self, value):
        node = Node(value)

        if self.end is None:
            self.start = node
            self.end = node
            self.count += 1
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
            self.count += 1

    def add_first(self,value):
        node = Node(value)

        temp = self.start
        self.start = node
        self.start.next = temp

    def add_last(self,value):
        node = Node(value)

        temp = self.end

        self.end.next = node
        self.end.prev = temp
        print(self.end.val)
        print(self.end.next.val)


    def __str__(self):
        list = []
        node = self.start
        while node is not None:
            list.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in list)}]"


mylist = dublyLinkedList()
mylist.add(1)
mylist.add(3)
mylist.add(5)
mylist.add_first(6)
print(mylist)
mylist.add_last(7)
print(mylist)

