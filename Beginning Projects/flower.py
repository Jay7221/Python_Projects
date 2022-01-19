#! python3
# flower.py

import turtle
from turtle_draw import arc

al = turtle.Turtle()

def petal(length, n):
    radius = length * 3 
    angle = 70
    arc(al, radius, angle)
    al.lt(110)
    arc(al, radius, angle)

def flower(length, n):
    angle = 70 + 70 + 110
    angle2 = 360/n 
    for i in range(n):
        petal(length, n)
        al.rt(angle)
        al.lt(angle2)

flower(100, 11)
    
