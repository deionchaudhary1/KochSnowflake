"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

tommy = turtle.Turtle()
tommy.color('blue')
tommy.penup()
tommy.speed(10000)
tommy.penup()
tommy.goto(-300,110)
tommy.pendown()
def koch(sideLength, level):
    if level > 0:
        for angle in [60, -120, 60, 0]:
            koch(sideLength/3, level-1)
            tommy.left(angle)
    else:
        tommy.forward(sideLength)

def snowFlake(sideLength, level):
  num = 3
  while num>0:
    koch(sideLength/3, level-1)
    tommy.right(120)
    num = num-1

# Test
koch(100, 0) #length of side is 100, level of 0 means no outer bend
tommy.pensize(3)
snowFlake(1000, 5)#length of side is 100, level of 1 means one outer bend


