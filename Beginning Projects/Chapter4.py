#! python3
# Chapter4.py

import string
import random

def change_base(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return change_base(n // base, base) + convert_string[n % base]

def rev_str(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + rev_str(string[:-1])

def is_pal(word):
    word = word.strip(string.punctuation + ' ').lower()
    if len(word) <= 1:
        return True
    else:
        if word[-1] == word[0]:
            return is_pal(word[1:-1])
        else:
            return False

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

def tree(branch_len, t):
    color = t.color()
    t.width(t.width() - 0.3)
    if branch_len > 5:
        if branch_len <= 15:
            t.color('green')
        else:
            t.color('brown')
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)
    t.width(t.width() + 0.3)
    t.color(color[0])

def natural_tree(branch_len, t):
    turtle.tracer(0, 0)
    color = t.color()
    flag = False
    if t.width() > 0.3:
        t.width(t.width() - 0.3)
        flag = True
    if branch_len > 5:
        angle = random.randrange(10, 50)
        if branch_len <= 15:
            t.color('green')
        else:
            t.color('brown')
        t.forward(branch_len)
        t.right(angle)
        red = random.randrange(5, 10)
        natural_tree(branch_len - red, t)
        t.left(2 * angle)
        red = random.randrange(5, 10)
        natural_tree(branch_len - red, t)
        t.right(angle)
        t.backward(branch_len)
    if flag:
        t.width(t.width() + 0.3)
    t.color(color[0])
    turtle.update()

def flower(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(60)
        tree(branch_len - 15, t)
        t.left(30)
        tree(branch_len - 15, t)
        t.left(30)
        tree(branch_len - 15, t)
        t.left(30)
        tree(branch_len - 15, t)
        t.left(30)
        tree(branch_len - 15, t)
        t.right(60)
        t.backward(branch_len)

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def sierpinkski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinkski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
        sierpinkski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, my_turtle)
        sierpinkski([points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])], degree - 1, my_turtle)
        

if __name__ == '__main__':
    import turtle
    t = turtle.Turtle()
    my_win = turtle.Screen()
    #my_points = ([-100, -50], [0, 100], [100, -50])
    #sierpinkski(my_points, 3, t)
    t.width(3)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    t.speed(0)
    natural_tree(100, t)
    my_win.exitonclick()



def pascal_triangle(n):
    '''Draw Pascal's triangle upto n layers.'''
    width = n * 5
    layer = 1
    layer_data = ['1']
    while layer <= n:
        print('  '.join(layer_data).center(width))
        layer_data = next_layer(layer_data)
        layer += 1


def next_layer(layer_data):
    current= None
    previous = None
    new_layer = list()
    while len(layer_data) > 0:
        current = int(layer_data.pop())
        if previous:
            new_layer.append(str(current + previous))
        else:
            new_layer.append(str(current))
        previous = current
    new_layer.append(str(current))
    return new_layer

#if __name__ == '__main__':
 #   pascal_triangle(4)
