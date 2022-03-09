import turtle
from random import randint


def move(x, y):
    global app_big_ball
    global apple_apple
    global ball_next
    global ball
    global ball_abs
    global app_big_ball_next

    turtle.goto(x, y)

    if abs(turtle.xcor() - app_big.xcor()) <= 10 and abs(turtle.ycor() - app_big.ycor()) <= 10: #с супер черепашкой
        app_big_ball_next += 5
        app_big_ball += 1
        ball_abs += 5
        if app_big_ball != app_big_ball_next:
            print(ball_abs)
            print('Удалить!')
            pen.goto(0, display_height / 2 - 50)

            pen.clear()
            pen.color('midnightblue')
            pen.write('Score = {}'.format(ball_abs), False, align='center', font=("Arial", 20, "normal"))

    if abs(turtle.xcor() - apple_1.xcor()) <= 10 and abs(turtle.ycor() - apple_1.ycor()) <= 10: #проверяет, когда черепашка попадает в мертвую черепашку
        ball_next += 1
        ball_abs += 1
    if ball != ball_next: #при попадании черепашка dead :(
        print(ball_abs)
        ball = ball_next
        apple_1.color('green')
        apple_1.hideturtle()
        if apple_1.isvisible() == False: # удалить, если невидима
            apple_1.showturtle()
            print('Удалить!')
            apple_1.goto(0,0)
            apple_1.penup()
            x = randint(-display_width / 2 + 100, display_width / 2 - 100)
            y = randint(-display_height / 2 + 100, display_height / 2 - 100)
            apple_1.color('red')
            apple_1.goto(x, y)

            pen.clear()
            pen.goto(0, display_height / 2 - 50)
            pen.color('midnightblue')
            pen.write('Score = {}'.format(ball_abs), False, align='center', font=("Arial", 20, "normal"))


def apple():
    apple_1 = turtle.Turtle()
    apple_1.shape('circle')
    apple_1.color('red')
    apple_1.penup()
    x = randint(-display_width / 2 + 100, display_width / 2 - 100)
    y = randint(-display_height / 2 + 100, display_height / 2 - 100)
    apple_1.goto(x, y)


ball_abs = 0 #ТОЧНОЕ ПОДСЧИТЫВАНИЕ БАЛЛОВ
# цвета, скорость и толщина
turtle.speed(8)
turtle.colormode(255) # цветовой режим
turtle.shapesize(0.5)

#screen дисплей
display = turtle.Screen()
display_width = 900
display_height = 600
display.setup(display_width, display_height)
display.bgcolor(102, 154, 156)

#текст
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

#начало писания (Score = 0, без .format)
pen.goto(0, display_height / 2 - 50)
pen.color('midnightblue')
pen.write('Score = 0', False, align='center', font=("Arial", 20, "normal"))

# рисование яблок
apple_1 = turtle.Turtle()
apple_1.speed(2)
apple_1.shape('circle')
apple_1.color('red')
apple_1.penup()
x = randint(-display_width / 2 + 100, display_width / 2 - 100)
y = randint(-display_height / 2 + 100, display_height / 2 - 100)
apple_1.goto(x, y)

apple_apple = 1

# курсор из черепашки
turtle.color(255, 182, 117)
turtle.shape('circle')

#подготовка к while
turtle.goto(0, 0)
ball = 0
ball_next = 0
turtle.penup()

# передвижение
turtle.onscreenclick(move)

app_big = turtle.Turtle()
app_big.speed(1)
app_big.shape('turtle')
app_big.color(15, 205, 15)
app_big.penup()
app_big_ball = 0
app_big_ball_next = 0
x_app = randint(-display_width / 2 + 100, display_width / 2 - 100)
y_app = randint(-display_height / 2 + 100, display_height / 2 - 100)
app_big.goto(x_app, y_app)

#while - цикл бесконечности
while True:
    x_app = randint(-display_width / 2 + 100, display_width / 2 - 100)
    y_app = randint(-display_height / 2 + 100, display_height / 2 - 100)
    app_big.goto(x_app, y_app)
    turtle.onscreenclick(move)


turtle.listen()
turtle.mainloop()