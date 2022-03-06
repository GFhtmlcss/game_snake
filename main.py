import turtle
from random import randint

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


def balls():
    print(turtle.position())


def goto():
    turtle_pos = turtle.position()
    return turtle_pos


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
apple_1 = turtle.Turtle()
apple_2 = turtle.Turtle()
apple_3 = turtle.Turtle()
apple_1.shape('circle')
apple_2.shape('circle')
apple_3.shape('circle')
apple_2.color('red')
apple_1.color('red')
apple_3.color('red')

apple_1.penup()
apple_2.penup()
apple_3.penup()
x = randint(-display_width / 2,display_width / 2)
y = randint(-display_height / 2, display_height / 2)
apple_1.goto(x, y)
x = randint(-display_width / 2, display_width / 2)
y = randint(-display_height / 2, display_height / 2)
apple_2.goto(x, y)
x = randint(-display_width / 2, display_width / 2)
y = randint(-display_height / 2, display_height / 2)
apple_3.goto(x, y)

# курсор из черепашки
turtle.color(255, 182, 117)
turtle.shape('circle')

#подготовка к while
turtle.goto(0, 0)
ball = 0
turtle.penup()

# передвижение

turtle.onscreenclick(turtle.goto)
x_range = range(apple_1.xcor() - 10, apple_1.xcor() + 10)
y_range = range(apple_1.ycor() - 10, apple_1.ycor() + 10)
apple_pos = x_range, y_range
x_t = range(turtle.xcor() - 10, turtle.xcor() + 10)
y_t = range(turtle.ycor() - 10, turtle.ycor() + 10)
turtle_pos = x_t, y_t
if turtle_pos in apple_pos:
    ball += 1
if ball == 1:
    print('УРА ПОБЕДА')

turtle.listen()
turtle.mainloop()