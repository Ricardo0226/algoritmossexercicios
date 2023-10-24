#1) Faça cada quadrado ter uma cor
#2) Faça cada quadrado com um formato diferente da tartaruga
#3) Faça os quadrados não se tocarem
#4) Desenhe um quadrado maior ao redor dos demais quadrados


import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.shape('turtle')
    turtle.color('blue')
    turtle.forward(100)
    turtle.right(90)

turtle.right(90)
turtle.penup()
turtle.backward(200)
turtle.pendown()



for _ in range(4):
   turtle.shape('square')
   turtle.color('yellow')
   turtle.left(90)
   turtle.forward(100)

turtle.right(180)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.forward(200)
turtle.pendown()

for _ in range(4):
   turtle.shape('circle')
   turtle.color('pink')
   turtle.forward(100)
   turtle.left(90)

turtle.left(90)
turtle.penup()
turtle.forward(400)
turtle.pendown()

for _ in range(4):
   turtle.shape('arrow')
   turtle.color('purple')
   turtle.right(90)
   turtle.forward(100)

turtle.right(180)
turtle.penup()
turtle.forward(100)
turtle.pendown()

for _ in range(4):
    turtle.shape('triangle')
    turtle.color('red')
    turtle.forward(200)
    turtle.right(90)

