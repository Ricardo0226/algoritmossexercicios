#Exercício

#1) Mude/defina a forma da tartaruga
#2) Mude a ordem das cores
#3) Mude a largura da linha
#4) Faça a tartaruga desenhar dois quadrados

import turtle

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.shape('turtle')

for color in ['black', 'blue', 'pink', 'red']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.backward(200)
turtle.pendown()

for color in ['black', 'blue', 'pink', 'red']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)