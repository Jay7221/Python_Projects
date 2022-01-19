#! python3
# ex15.py

import math, copy, turtle, turtle_draw

class Point:
    '''A class to represent a point.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class rectangle:
    '''A class to represent a rectangle.'''
    def __init__(self, height, width, corner):
        self.height = height
        self.width = width
        self.corner = copy.deepcopy(corner)
        self.corner2 = shift_point(corner, width, 0)
        self.corner3 = shift_point(corner, width, height)
        self.corner4 = shift_point(corner, 0, height)
        
class Circle:
    '''A class to represent circle.'''
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

def shift_point(point, x, y):
    new_point = copy.deepcopy(point)
    new_point.x += x
    new_point.y += y
    return new_point


def distance(p1, p2):
    dist = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    dist = math.sqrt(dist)
    return dist

def point_in_circle(circle, point):
    dist = distance(circle.center, point)
    if dist <= circle.radius:
        return True
    else:
        return False

def rect_in_circle(circle, rect):
    flag = True
    for corner in [rect.corner, rect.corner2, rect.corner3, rect.corner4]:
        if not point_in_circle(circle, corner):
            flag = False
    return flag
            
def draw_rect(t, rect):
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    
def draw_circle(t, circle):
    turtle_draw.circle(t, circle.radius)
