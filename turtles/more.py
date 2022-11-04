import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
color("red")
left(90)

for i in range(250):
    left(120)
    forward(i*2)

for i in range(250):
    right(120)
    forward(i*2)

#left(90)
#for i in range(250):
    #left(120)
    #forward(i*2)
    #right(120)
    #forward(i/2)


done()