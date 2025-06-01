import turtle
t = turtle.Turtle()
t.color((.5, 1, 0))
for i in range(8):
    t.circle(50)
    t.left(45)
t.write("Çizim bitti!")
turtle.done()

import turtle

for a in range(20):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.right(5)
input()