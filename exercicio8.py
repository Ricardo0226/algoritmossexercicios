#1) Acrescente cores
#2) Mude a largura da linha
#3) Aumente a quantidade de linhas

import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'black', 'brown', 'red']
for _ in range (16):
    color = random.choice(colors)
    turtle.color(color)
    turtle.right(50)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)