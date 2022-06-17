import turtle
def draw_fractal(level, pen):
    pen.fd(level * 10)
    if level > 1:
        turn_right(pen)
        draw_fractal(level - 1, pen)
        turn_left(pen)
        turn_left(pen)
        draw_fractal(level - 1, pen)
        turn_right(pen)
    pen.bk(level * 10)

def turn_right(pen):
    pen.rt(30)

def turn_left(pen):
    pen.lt(30)

pen = turtle.Turtle()
pen.lt(90)
draw_fractal(5, pen)