#! python3
# list_data_structure.py



class Node():
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return str(self.data)

class UList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __repr__(self):
        result = str()
        current = self.head
        result += '['
        while current != None:
            result += str(current.data) + ', '
            current = current.get_next()
        result = result[:-2]
        result += ']'
        return result
    __str__ = __repr__

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self.tail == None:
            self.tail = temp
            
        current = self.head.get_next()
        self.len += 1

    def size(self):
        return self.len
    

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current == None:
            print('No such item exists.')
        else:
            self.len -= 1

            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
                current = previous.get_next()

    def slice(self, start, stop):
        '''Return an UList items from start to stop not including item at stop.'''
        index = 0
        current = self.head
        new_list = UList()
        if start > self.size() or stop > self.size() or start > stop:
            return 'Invalid Parameters'
        while index != start:
            index += 1
            current = current.get_next()
        while index != stop:
            index += 1
            new_list.append(current.data)
            current = current.get_next()
        return new_list
            

    def append(self, item):
        if self.tail == None:
            temp = Node(item)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(item)
            self.tail.set_next(temp)
            self.tail = temp
        self.len += 1
        '''current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()
        if self.size() != 0:
            current = Node(item,  self.size())
            previous.set_next(current)
        else:
            self.add(item)'''

    def print_data(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.get_next()

    def insert(self, index, item):
        current = self.head
        previous = None
        while self.index(current.data) != index:
            previous = current
            current = current.get_next()
        new_node = Node(item)
        previous.set_next(new_node)
        new_node.set_next(current)
        

    def index(self, item):
        index = 0 
        current = self.head
        while current.data != item:
            index += 1
            current = current.get_next()
        return index

    def pop(self, index = 0):
        current = self.head
        while self.index(current.data) != index:
            current = current.get_next()
        self.remove(current.data)
        return current.data
        
class OrderedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        result = str()
        current = self.head
        result += '['
        while current != None:
            result += str(current.data) + ', '
            current = current.get_next()
        result = result[:-2]
        result += ']'
        return result

    def is_empty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        
        if previous == None:
            temp = Node(item)
            if current == None:
                self.head = temp
            else:
                temp.set_next(self.head)
                self.head = temp
        else:
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)
            

        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            

    def print_data(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.get_next()

    def pop(self, index = 0):
        current = self.head
        while self.index(current.data) != index:
            current = current.get_next()
        self.remove(current.data)
        return current.data

    def index(self, item):
        index = 0 
        current = self.head
        while current.data != item:
            index += 1
            current = current.get_next()
        return index
    
            
if __name__ == '__main__':
    ul = UList()
    for i in range(1000):
        ul.append(i)
    ol = OrderedList()
    for i in range(1000):
        ol.add(i)

    l = list()
    for i in range(1000):
        l.append(i)

    from timeit import Timer

    ul_list_pop = Timer('ul.pop()', 'from __main__ import ul')
    list_pop = Timer('l.pop()', 'from __main__ import l')
    ol_list_pop = Timer('ol.pop()', 'from __main__ import ol')
    print('ul_pop', ul_list_pop.timeit(number = 1000),'ol_pop', ol_list_pop.timeit(number = 1000),'list_pop', list_pop.timeit(number = 1000))
