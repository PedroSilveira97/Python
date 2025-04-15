from turtle import Turtle, Screen
import random
import tkinter as tk
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("", prompt="Choose a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]
turtles = []

g = Turtle()
g.penup()
g.goto(x=205, y=100)
g.setheading(270)
g.pendown()
g.forward(200)

def display_winner(a, b):
    result_window = tk.Tk()
    result_window.title("Race Result")
    result_window.geometry("300x100")

    if a == b:
        result_text = f"The {a} turtle won. You win!"
    else:
        result_text = f"The {a} turtle won. You lose!"

    label = tk.Label(result_window, text=result_text, font=("Arial", 16))
    label.pack(pady=20)

    result_window.mainloop()


for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y_pos[turtle_index])
    turtles.append(t)


race = True

while race:
    for t in turtles:
        if t.xcor() > 200:
            race = False
            winner = t.pencolor()
            display_winner(winner, bet)
        random_distance = random.randint(1, 10)
        t.forward(random_distance)

screen.exitonclick()
