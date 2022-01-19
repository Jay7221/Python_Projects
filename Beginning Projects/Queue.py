
#! python
# Queue.py

class Queue():
    def __init__(self):
        self.items = list()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    __str__ = __repr__
