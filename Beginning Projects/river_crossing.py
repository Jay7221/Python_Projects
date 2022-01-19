#! python3
# river_crossing.py

import turtle

degree = 0
def cross_river(num):
    global degree
    degree += 1
    if num > 1:
        cross_river(num - 1)
        move_boat('monk', 'cannibal')
        return_boat('cannibal')
        move_boat('cannibal', 'cannibal')
        return_boat('cannibal')
    if degree == 1:
        move_boat('monk', 'cannibal')
    degree -= 1

def move_boat(*args):
    names = ' and '.join(args)
    print('Moving %s from shore.'%names)

def return_boat(*args):
    names = ' and '.join(args)
    print('Returning %s to shore.'%names)

if __name__ == '__main__':
    cross_river(3)


