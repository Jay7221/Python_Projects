#! python3
# Stack.py

class Stack():
    '''An abstract data type'''
    def __init__(self):
        self.items = list()
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)
