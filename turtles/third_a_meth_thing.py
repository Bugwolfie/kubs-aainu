import turtle
from turtle import *
import math

sc = turtle.Screen()
sc.title('just for her smile')
sc.bgcolor('black')

inu = turtle.Turtle()

inu.speed(20)
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()

inu.penup()
inu.forward(200)
inu.pendown()
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()

inu.penup()
inu.forward(200)
inu.pendown()
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()

inu.penup()
inu.backward(100)
inu.pendown()
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()

inu.penup()
inu.backward(100)
inu.pendown()
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()

inu.penup()
inu.backward(200)
inu.pendown()
inu.begin_fill()
inu.color("#CFAFBD","#633498")
for i in range(100):
    inu.forward(math.sqrt(i)*10)
    inu.left(170.62)
inu.end_fill()



turtle.done()