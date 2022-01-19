#! python3
# turtle_draw.py

import math
import turtle
bob = turtle.Turtle()

def polygon(t, length, n):
    '''Here t is the turtle object, length is the length of sides of polygon, and n is the number of sides of the polygon.'''
    angle = 360 / n
    polyline(t, n, length, angle)

def circle(t, radius):
    arc(t, radius, 360)

def arc(t, radius, angle):
    '''Draws an arc of radius and angle(in degrees).'''
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    turn_angle = angle / n
    polyline(t, n, step_length, turn_angle)

    
def polyline(t, n, length, angle):
    '''Draws a n lines of length and turns angle(in degrees) after each line.'''
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def pie(t, n, length):
    angle = 360 / n
    angle2 = 90 - angle/2
    diagonal = length /(2 * math.sin(angle / 2)) 
    for i in range(n):
        t.fd(length)
        t.lt(angle + angle2)
        t.fd(-diagonal)
        t.rt(180 - angle)
        t.fd(-diagonal)
        t.rt(angle)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)

def koch(t, length):
    if length < 5:
        t.fd(length)
    else:
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)
        t.rt(120)
        koch(t, length/3)
        t.lt(60)
        koch(t, length/3)

def interesting(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    interesting(t, length, n - 1)
