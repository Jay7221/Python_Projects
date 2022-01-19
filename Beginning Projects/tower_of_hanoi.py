#! python3
# tower_of_hanoi.py

from Stack import Stack
import turtle

step = 0
def move_tower(height, from_pole, to_pole, with_pole):
    '''Moves tower height = height from pole from_pole to to_pole using with_pole as intermediate.'''
    global step
    if height >= 1:
        step = move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        print(from_pole.name, from_pole, to_pole.name, to_pole, with_pole.name, with_pole)
        step = move_tower(height - 1, with_pole, to_pole, from_pole)
    temp = step
    step = 0
    return temp
        

def move_disk(from_pole, to_pole):
    print('Moving disk %s from'%from_pole.peek(), from_pole.name, to_pole.name)
    to_pole.push(from_pole.pop())
    global step
    step += 1

if __name__ == '__main__1':
    T1 = Stack()
    T2 = Stack()
    T3 = Stack()
    T1.name = 'tower1'
    T2.name = 'tower2'
    T3.name = 'tower3'
    for i in range(1, 6).__reversed__():
        T1.push(i)
    move_tower(5, T1, T2, T3)

def animate_towers(height, from_pole, to_pole, with_pole):
    pen = turtle.Turtle()
    pen.left(90)
    pen.right(90)
    pen.fd(40 + 5 * height)
    pen.left(90)
    pen.fd(200)
    pen.fd(-200)
    for i in range(2):
        pen.left(90)
        pen.fd(40 + 5 * height)
        pen.right(90)
        pen.fd(200)
        pen.fd(-200)
    pen.right(90)
    pen.fd(40 + 5 * height)
    pen.left(90)

class Tower:
    def __init__(self, name, base_x, base_y = 0, height = 200, num_disks = 0):
        self.base_x = base_x
        self.base_y = base_y
        self.height = height
        self.num_disks = num_disks
        self.disks = Stack()
        self.name = name

    def draw(self, t):
        t.up()
        t.pensize(10)
        t.goto(self.base_x, self.base_y)
        t.down()
        t.goto(self.base_x, self.base_y + self.height)

    def move_disk(self, to_tower):
        disk = self.disks.pop()
        disk.turtle.goto(self.base_x, self.base_y + self.height + 10)
        self.num_disks -= 1
        disk.move(to_tower)
        print('Moving %s from %s to %s.' %(disk.name, self.name, to_tower.name))
        

class disk:
    def __init__(self, width, tower, name):
        self.turtle = turtle.Turtle()
        self.turtle.up()
        self.turtle.shape('square')
        self.turtle.turtlesize(1, width, 1)
        self.move(tower)
        self.name = name

    def move(self, to_tower):
        self.turtle.goto(to_tower.base_x, to_tower.base_y + to_tower.height + 10)
        self.turtle.goto(to_tower.base_x, to_tower.base_y + to_tower.num_disks * 15 + 5)
        to_tower.num_disks += 1
        to_tower.disks.push(self)
        


def animate_towers_of_hanoi(num_disks):
    pen = turtle.Turtle()
    from_tower = Tower('from_tower', -num_disks * 25 - 150)
    with_tower = Tower('with_tower', 0)
    to_tower = Tower('to_tower', num_disks * 25 + 150)
    from_tower.draw(pen)
    with_tower.draw(pen)
    to_tower.draw(pen)
    pen.hideturtle()
    width = 3 + num_disks
    for i in range(num_disks).__reversed__():
        disk(width, from_tower, i + 1)
        width -= 1
    height = from_tower.num_disks
    animate_move_tower(height, from_tower, to_tower, with_tower)
    
        
def animate_move_tower(height, from_tower, to_tower, with_tower):
    if height >= 1:
        animate_move_tower(height - 1, from_tower, with_tower, to_tower)
        from_tower.move_disk(to_tower)
        animate_move_tower(height - 1, with_tower, to_tower, from_tower)

if __name__ == '__main__':
    animate_towers_of_hanoi(4)






