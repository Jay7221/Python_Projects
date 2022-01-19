#! python3
# nodes.py

class Node:
    '''Class representing one node ina linked list.'''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    '''Class representing a linked list data structure.'''

    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        '''Add a new node to the linked list.'''
        previous_head = self.head
        self.head = Node(data)
        previous_head.previous = self.head
        self.head = previous_head
        
