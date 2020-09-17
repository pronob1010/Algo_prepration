class Node():
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None
        self.count = 0

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
        self.count += 1

    def add_last(self,value):
        node = Node(value)

        temp = self.end
        self.end.next = node
        self.end.prev = temp
        self.count += 1

    def replaceByPosition(self,pos1,pos2):
        pos = 0
        posc = 0
        temp1 = None
        temp2 = None
        current = self.start
        while current is not None:
            if pos is pos1:
                temp1 = current
                temp1prev = temp1.prev
                temp1next = temp1.next
                print(temp1prev,"-",temp1.val,"-",temp1next.val)

            if pos is pos2:
                temp2 = current
                temp2prev = temp2.prev
                temp2next = temp2.next
                print(temp2prev.val, "-", temp2.val, "-", temp2next.val)

            pos += 1
            current = current.next


        current2 = self.start
        while current2 is not None:
            if posc is pos1:
                current2.next = temp2next
                current2.val = temp2.val
                current2.prev = temp2prev


            if posc is pos2:
                current2.next = temp1next
                current2.val = temp1.val
                current2.prev = temp1prev

            posc += 1
            current2 = current2.next



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
print("total element : ", mylist.count)

# pos1, pos2 = list(map(int, input("Enter 2 position that you want to replace : ").split()))
pos1 =1
pos2 =3
print("pos1 ",pos1)
print("pos2 ",pos2)

mylist.replaceByPosition(pos1,pos2)
print(mylist)
