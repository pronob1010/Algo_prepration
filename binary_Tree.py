class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.item = value

    def insert(self, value):
        if self.item:
            if value< self.item:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)

            elif value>self.item:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def search(self, value):
        f = 0
        if self.item != None:
            if value == self.item:
                print("%d is Found"%(self.item))
                f = 1
            elif value < self.item:
                if self.left != None:
                    self.left.search(value)
            elif value > self.item:
                if self.right != None:
                    self.right.search(value)
        return f

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.item)
        if self.right:
            self.right.printTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(5)

root.printTree()
x = root.search(15)
if x == 0:
    print("Not Found")