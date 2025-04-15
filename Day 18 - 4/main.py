import turtle as tm
import colorgram
import random

rgb = []
colors = colorgram.extract("day 18.jpg", 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb.append(new_color)

print(rgb)
tm.colormode(255)
t = tm.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
total_dots = 100
for dot_count in range(1, total_dots + 1):
    t.dot(20, random.choice(rgb))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = tm.Screen()
screen.exitonclick()
