class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.item = value

    def printTree(self):
        print(self.item)

root = Node(10)
root.printTree()