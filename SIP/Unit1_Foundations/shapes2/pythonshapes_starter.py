from turtle import *
import math
sides=int(input("Please enter the number of sides:"))
#color=input("Please enter a color: ")
# Name your Turtle.

t = Turtle()
t.pencolor("red")
t.penup()
# Set Up your screen and starting position.
setup(500,300)
x = -250
y = -150
t.setposition(x, y)
t.pendown()
### Write your code below:
for i in range(sides):
    t.pendown()
    t.right(360/sides)
    t.forward(100)
t.penup()
"""
t.goto((x*-1),(y*-1))

for i in range(3):
    t.pendown()
    t.right(120)
    t.forward(100)



# Close window on click.
exitonclick()
"""
