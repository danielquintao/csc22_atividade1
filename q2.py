import turtle


def draw_poly(t, n, sz):
    turn = 180 - (n - 2) * 180 / n
    for _ in range(n):
        t.forward(sz)
        t.left(turn)


# test
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("#98ed80")  # verde limao

    tess = turtle.Turtle()
    tess.color("#be93e6")
    tess.width(3)

    draw_poly(tess, 8, 50)

    screen.mainloop()

