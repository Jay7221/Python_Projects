#! python3
# HashTable.py

class HashTable:
    def __init__(self, size = 11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.len = 0

    def extend(self, size):
        slots = self.slots
        data = self.data
        self.__init__(size)
        for k, v in zip(slots, data):
            self[k] = v

    def put(self, key, data):
        
        if self.len == self.size:
            self.extend(self.size * 2)

            
        hash_value = self.hash_function(key, len(self.slots))
                

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # Replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data # Replace
        self.len += 1

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size, step_size = 1):
        return (old_hash + step_size) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def put_q(self, key, data):
        
        if self.len == self.size:
            self.extend(self.size * 2)

            
        hash_value = self.hash_function(key, len(self.slots))

        step_size = 1

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # Replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots), step_size ** 2)
                step_size += 1
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots), step_size ** 2)
                    step_size += 1

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data # Replace
        self.len += 1

    def get_q(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        step_num = 1
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots), step_num ** 2)
                step_num += 1
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def __contains__(self, item):
        if item in self.data:
            return True
        else:
            return False

    def __len__(self):
        return self.len

    def __delitem__(self, key):
        self.data.remove(self[key])
        self.slots.remove(key)
        slots = self.slots
        data = self.data
        size = self.size
        self.__init__(size)
        for k, v in zip(slots, data):
            if k:
                self[k] = v

if __name__ == '__main__':
    a = HashTable()
    for i in range(50):
        a[i**2] = i
