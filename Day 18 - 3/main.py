from turtle import Turtle
import random
colour = ["medium blue", "firebrick", "lime green", "dark red", "dark violet",
          "dark gray", "dark olive green", "yellow", "dark orange"]
turtle = Turtle()
turtle.home()
turtle.shape("turtle")
turtle.teleport(0, 50)


def draw(shape):
    angle = 360/shape
    for _ in range(shape):
        turtle.forward(100)
        turtle.right(angle)


for i in range(3, 11):
    turtle.color(random.choice(colour))
    draw(i)
