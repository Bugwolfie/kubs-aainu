import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
color("red")
left(90)
for i in range(250):
    right(120)
    forward(i)
    left(60)
    forward(i)
for i in range(750,0,-1):
    right(120)
    forward(i/3)
    left(60)
    forward(i/3)







done()