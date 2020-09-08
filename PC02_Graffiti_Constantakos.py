#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)
panel.bgcolor("red")

t = Turtle()
t.shape('turtle')
t.speed(10)
t.up()
t.goto(200,200)
t.down()
t.color("green")
t.circle(70)
t.pensize(10)
t.up()
t.goto(-20,200)
t.down()
t.color("yellow")
t.circle(50)
t.up()
t.pensize(50)
t.begin_fill()
t.color("blue")
t.goto(-200,-180)
t.down()
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.up()
t.right(90)
t.down()
t.forward(100)
t.end_fill()
t.up()
t.goto(100,-200)
t.down()
t.pensize(5)
t.color("pink")
t.begin_fill()
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.right(40)
t.forward(40)
t.up()
t.down()
t.up()
t.down()
t.right(40)
t.forward(40)
t.end_fill()
















