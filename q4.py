import turtle


def spiral(t, sz0, delta, angle=90):
    t.right(90)
    delta = - abs(delta)
    for sz in range(sz0, 0, delta):
        t.forward(sz)
        t.left(angle)


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("#98ed80")

    tess = turtle.Turtle()
    tess.color("blue")
    tess.width(1)

    initial_pos = tess.pos()
    print(initial_pos)

    spiral(tess, 100, 2)

    tess.penup()
    tess.goto(initial_pos + (120., 0.))
    tess.seth(0)
    tess.pendown()

    spiral(tess, 100, 2, angle=89)

    screen.mainloop()
