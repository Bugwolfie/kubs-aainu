import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
color("red")
left(90)
for i in range(250):
    right(140)
    forward(i)
    left(70)
    forward(i)
for i in range(750,50,-1):
    right(140)
    forward(i/3)
    left(70)
    forward(i/3)







done()