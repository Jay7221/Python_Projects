#! python3
# binary_tree.py

class Node:
    '''Binary tree node.'''

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    '''This class represents a binary tree data structure.'''
    def __init__(self, root):
        self.root = Node(root)
        self.root.left = None
        self.root.right = None

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        


def breadth_first(tree):

    current_level = [tree.root]
    next_level = []

    while current_level:
        for node in current_level:
            print(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            current_level = []
            for i in next_level:
                current_level.append(i)
            next_level = []
