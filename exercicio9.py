#1) Faça cada passo da tartaruga ter uma cor diferente
#2) Aumente/diminua o diâmetro do círculo


import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'red', 'black']
for c in range(360):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(3)
    turtle.right(1)

