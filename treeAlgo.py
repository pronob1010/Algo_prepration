class Node():
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None

class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def PreOrderView(self, start, string):
        if start:
            string += (str(start.value) + "-")
            string = self.PreOrderView(start.left, string)
            string = self.PreOrderView(start.right, string)

        return string


tree = BinarySearchTree.root(0)
tree.left = Node(1)
tree.right = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(5)
tree.right.left = Node(4)
tree.right.right = Node(5)

print(tree.PreOrderView(tree.root, " "))
print(tree.PreOrderView(tree.left, " "))
print(tree.PreOrderView(tree.right, " "))