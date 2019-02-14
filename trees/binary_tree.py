class BinaryTree:
    def __init__(self, root=None):
        self.root = root


class Node:

    def __init__(self, data, parent=None, l_child=None, r_child=None):
        self.data = data
        self.parent = parent
        self.left = l_child
        self.right = r_child
