import turtle

screen = turtle.Screen()
screen.bgcolor("#98ed80")  # verde limao

t = turtle.Turtle()
t.color("#be93e6")
t.width(3)

for sz in range(100, 0, -20):
    # desenha quadrado:
    t.forward(sz)
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)
    # vai para ponto inicial de proximo quadrado
    t.penup()
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

# para abaixo do circulo
t.penup()
t.right(90)
t.forward(60)
t.right(90)
t.forward(60)
t.right(180)

screen.mainloop()
