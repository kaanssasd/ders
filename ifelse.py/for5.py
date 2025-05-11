import math, random as r
from turtle import *


renkler=["red","green","blue"]
print(r.random())
print(r.randint(50,100))
print(r.choice(renkler))
speed(10)
for ddd in range (10):
    kenaru = r.randint(50,200)
    color(r.choice(renkler))
    aa=r.randint(-300,300)
    ss=r.randint(-300,300)
    penup()
    goto(aa,ss)
    pendown()
    for a in range(4):
        forward(kenaru); right(90)
input()