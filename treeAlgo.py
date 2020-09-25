class Node():
    def __init__(self, val):
        self.left = None
        self.value = val
        self.right = None

class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def PreOrderView(self, val):
        if val

tree = BinarySearchTree(1)
tree.left = Node(2)
tree.left.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(tree.right.value)
