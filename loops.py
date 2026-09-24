import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(x,y):
    t.left(5)
    for i in range(5):
        t.speed(0)
        t.forward(x)
        t.left(y) # type: ignore
square(5, 144)
"""    
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)
 """
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 144)
        length += 5
addSquares(60)



