import turtle
from turtle import *

sc = turtle.Screen()
sc.title('just for her smile')
sc.bgcolor('black')

inu = turtle.Turtle()

inu.speed(10)
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(200)
    inu.left(170.62)
inu.end_fill()




turtle.done()