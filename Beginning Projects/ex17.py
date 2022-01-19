#! python3
# ex17.py

class Kangaroo():
    '''A class to represent a kangaroo.'''

    def __init__(self, name, contents = None):
        self.name = name
        if contents == None:
            self.pouch_contents = []
        else:
            self.pouch_contents = contents
        
    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)

    def __str__(self):
        return str(self.pouch_contents)



