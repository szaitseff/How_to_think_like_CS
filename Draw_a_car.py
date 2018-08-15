#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     14.01.2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def draw_rectangle(t, w, h, clr):
    """Get turtle t to draw a rectangle with width w, hight h and color clr."""
    t.pendown()
    t.color(clr, clr)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.penup()
    t.home()

def draw_circle(t, r, angle, clr):
    """Get turtle to draw a circle with radius r and color clr;
    angle = 360 for a full circle, 180 for semicircle, etc."""
    t.pendown()
    t.color(clr, clr)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
    tess.home()

def draw_poly(t, n, sz, clr):
    """Get turtle to draw a regular polygon with a side sz and color clr."""
    t.pendown()
    t.color(clr, clr)
    t.begin_fill()
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    t.end_fill()
    t.penup()
    tess.home()

def draw_triangle(t, x, y, clr):
    """Get turtle to draw a triangle with sides x and y and color clr."""
    t.pendown()
    t.color(clr, clr)
    t.begin_fill()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.end_fill()
    t.penup()
    tess.home()

import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(0)
tess.penup()

tess.goto(0, 0)
draw_rectangle(tess, 450, 100, "green") # the car body

tess.goto(-200, 0)
draw_triangle(tess, 200, 100, "green")  # a front spoiler
tess.goto(-200,0)
draw_triangle(tess, 60, 40, "white")

tess.goto(380, 120)
draw_triangle(tess, 80, 20, "green")  # a rear spoiler
tess.goto(420, 100)
draw_rectangle(tess, 15, 20, "green")

tess.goto(50,-50)
draw_circle(tess, 50, 360, "black")  # front wheels
tess.goto(50, 0)
tess.dot(15, "white")

tess.goto(350,-50)
draw_circle(tess, 50, 360, "black")  # rear wheels
tess.goto(350, 0)
tess.dot(15, "white")

tess.goto(100, 100)
draw_rectangle(tess, 200, 80, "green") # cabin

tess.goto(0,100)
draw_triangle(tess, 100, 80, "blue")  # front window

tess.goto(300, 180)
tess.right(90)
draw_triangle(tess, 80, 80, "blue")   # rear window

tess.goto(120, 100)
draw_rectangle(tess, 160, 65, "blue")  # side windows

tess.goto(-140, 10)
draw_rectangle(tess, 15, 20, "yellow") # front lights

tess.goto(450, 70)
tess.left(180)
draw_rectangle(tess, 10, 25, "red")  # rear lights

tess.color("white")
tess.goto(-100, -100)

wn.mainloop()

