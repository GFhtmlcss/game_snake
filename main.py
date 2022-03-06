import turtle
from random import randint


def move(x, y):
    global apple_apple
    global ball_next
    global ball
    turtle.goto(x, y)
    if abs(turtle.xcor() - apple_1.xcor()) <= 10 and abs(turtle.ycor() - apple_1.ycor()) <= 10: #проверяет, когда черепашка попадает в мертвую черепашку
        ball_next += 1
    if ball != ball_next: #при попадании черепашка dead :(
        print(ball_next)
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

        apple_apple = 0
        return apple_apple

def apple():
    apple_1 = turtle.Turtle()
    apple_1.shape('circle')
    apple_1.color('red')
    apple_1.penup()
    x = randint(-display_width / 2 + 100, display_width / 2 - 100)
    y = randint(-display_height / 2 + 100, display_height / 2 - 100)
    apple_1.goto(x, y)


# цвета и скорость
turtle.speed(8)
turtle.colormode(255) # цветовой режим
turtle.shapesize(0.5)

#screen дисплей
display = turtle.Screen()
display_width = 900
display_height = 600
display.setup(display_width, display_height)
display.bgcolor(110, 110, 50)

# рисование яблок
apple_1 = turtle.Turtle()
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

#while - цикл бесконечности
for i in range(100):
    turtle.onscreenclick(move)


turtle.listen()
turtle.mainloop()