import turtle
from turtle import *
import math
import random 

sc = turtle.Screen()
sc.title('just for her smile')
sc.bgcolor('black')

inu = turtle.Turtle()

inu.speed(10)
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(10)
    inu.left(math.sin(i*60)*35)
    inu.left(45)
inu.end_fill()




turtle.done()