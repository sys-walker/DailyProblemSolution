#!/usr/bin/python3

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()


def invert(node):
    if node != None:
        invert(node.left)
        invert(node.right)

        node_temp = node.left
        node.left = node.right
        node.right = node_temp


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')

    root.preorder()

    # a b d e c f
    print("\n")
    invert(root)
    root.preorder()
    # a c f b e d

