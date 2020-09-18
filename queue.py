class Node():
    def __init__(self,val):
        self.prev = None
        self.value = val
        self.next = None

class doublylinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.count +=1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.count +=1

    def pop(self):
        if self.head is not None:
            poped_element = self.head.value
            newlast = self.head.next
            self.head = newlast
            self.count -=1
            print("Poped element : ",poped_element)

    def __str__(self):
        list = []
        node = self.head
        while node is not None:
            list.append(node.value)
            node = node.next
        return f"[{', '.join(str(val) for val in list)}]"


mylist = doublylinkedlist()
mylist.push(1)
mylist.push(3)
mylist.push(5)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop()
print(mylist)
mylist.push(5)
print(mylist)
mylist.push(6)
print(mylist)
mylist.pop()
print(mylist)
