#import turtle
#tinny= turtle.Turtle()
#print(tinny)
#from turtle(module) import Turtle(class)
#tinny=Turtle()

from turtle import Turtle, Screen
#Screen class from the turtle module in Python.
tinny=Turtle()
print(tinny)
tinny.shape("turtle")
tinny.color("burlywood4", "DarkSlateGray")
tinny.forward(200)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
