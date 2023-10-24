
#1) Aumente o tamanho do envelope
#2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
#3) Deixe o envelope colorido
#4) Reduza o aba do envelope
#"""

import turtle
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)
turtle = turtle.Turtle()


for _ in [1, 2, 3, 4]:
  turtle.shape("arrow")
  pen_color=random_color()
  turtle.pencolor(pen_color)
  turtle.forward(200)
  turtle.right(90)
turtle.forward(200)
for _ in [1, 2]:
    turtle.shape("turtle")
    pen_color=random_color()
    turtle.pencolor(pen_color)
    turtle.right(160)
    turtle.forward(110)
    turtle.left(120)
