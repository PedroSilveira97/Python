from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("circle")
turtle.color("firebrick2")
turtle.teleport()
y = random.randint(1, 480)
x = random.randint(1, 640)
turtle.teleport()
screen = Screen()
screen.exitonclick()
