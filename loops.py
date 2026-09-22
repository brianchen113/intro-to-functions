import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
turtle.done()

def square(x,y):
    for i in range(60):
        t.forward(x)
        t.left(y) # type: ignore
square(4, 90)
"""    
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)
 """
""" def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5) """



