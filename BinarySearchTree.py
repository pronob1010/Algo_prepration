class Node():
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None

class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def PreOrderView(self, start,string):
        if start:
            string += (str(start.value) + "->")
            # string = start.value
            #             # print(string)
            string = self.PreOrderView(start.left,string)
            string = self.PreOrderView(start.right,string)

        return string

    def PostOrderView(self, start,string):
        if start:
            string += (str(start.value) + "->")
            # string = start.value
            # print(string)
            string = self.PreOrderView(start.right,string)
            string = self.PreOrderView(start.left,string)

        return string

    def InOrderView(self, start,string):
        if start:
            string = self.InOrderView(start.left,string)
            string += (str(start.value) + "->")
            # string = start.value
            # print(string)
            string = self.InOrderView(start.right,string)

        return string


tree = BinarySearchTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right = Node(9)

print("Pre-Order View:",tree.PreOrderView(tree.root, " "))#[" " this  is for set a string, we can a make a print function to optimize this ]
print("Post-Order View:",tree.PostOrderView(tree.root, " "))
print("In-Order View:",tree.InOrderView(tree.root, " "))
