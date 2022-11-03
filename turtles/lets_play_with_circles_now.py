import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
left(90)
forward(50)
for i in range(150):
    color("#40E0D0")
    circle(i*0.7)
    color("#0A5044")
    circle(i*0.5)
    right(3)
    forward(3)
color("black")

for i in range(150,0,-1):

    color("#40E0D0")
    circle(i*0.7)
    color("#0A5044")
    circle(i*0.5)
    right(3)
    forward(3)




done()