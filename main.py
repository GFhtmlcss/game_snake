import turtle
from random import randint
import time


def right():
    turtle.setheading(0)
    turtle.fd(50)

def left():
    turtle.setheading(180)
    turtle.fd(100)

def top():
    turtle.setheading(90)
    turtle.fd(50)

def bottom():
    turtle.setheading(270)
    turtle.fd(100)

def apple():
    turtle.color(200, 50, 2)
    turtle.penup()
    x = randint(-display_width / 2, display_width / 2)
    y = randint(-display_height / 2, display_height / 2)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


def balls():
    print(turtle.position())


# цвета и скорость
turtle.speed(8)
turtle.colormode(255) # цветовой режим
turtle.shapesize(0.5)

#screen дисплей
display = turtle.Screen()
display_width = 900
display_height = 600
display.setup(display_width, display_height)
display.bgcolor(30, 50, 0)

# рисование яблок
apple()
x_y_1 = turtle.position()
apple()
x_y_2 = turtle.position()
apple()
x_y_3 = turtle.position()


# курсор из черепашки
turtle.color(255, 182, 117)
turtle.shape('circle')

# передвижение
turtle.penup()
turtle.goto(0, 0)
ball = 0
turtle.onscreenclick(turtle.goto)


turtle.listen()
turtle.mainloop()