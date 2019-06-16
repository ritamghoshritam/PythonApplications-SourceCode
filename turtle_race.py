from turtle import *
from random import randint
speed(10)
goto(-140,140)

penup()

for step in range(20):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

mon = Turtle()
mon.color('green')
mon.shape('turtle')

mon.penup()
mon.goto(-160, 90)
mon.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    mon.forward(randint(1,5))
