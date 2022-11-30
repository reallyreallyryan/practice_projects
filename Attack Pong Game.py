# Trying Pong Tutorial to learn Python
# Followed tutorial from freecodeacademy, made some adjustments
# Adjustments Include:
    # Both paddles can now move up, down, left,and right. The ball bounces off the paddles, regardless of where they are (to a point).
    # Adjust the look and added sound for a goal
    # One current problem I need to solve is making it so the ball doesn't 'stick' if you move the paddle while the ball is close to it.
    # I'm going to come back when I've leveled up. 

import turtle
import os


#Window
wn = turtle.Screen()
wn.title("Attack Pong!")
wn.bgcolor('grey')
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=3, stretch_len=2)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('blue')
paddle_b.shapesize(stretch_wid=3, stretch_len=2)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Red: 0  Blue: 0", align="center", font=("Courier", 24, "normal"))

#Functions
    #Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

    #Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)

#Keybord Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right,"d")
wn.onkeypress(paddle_a_left, "a")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_right, "Right")
wn.onkeypress(paddle_b_left, "Left")

# Main Game Loop
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay beep.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay beep.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        os.system("afplay goal.wav&")
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("afplay goal.wav&")
        pen.clear()
        pen.write("Red: {}  Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

   #Paddle + Ball Collision
    #IF ball is near border of window AND the ball is between the edges of the paddle, set ball to (340) and then reverse order
    #Im going to attempt to make the ball bounce off the paddle, regardless of where it is. ->
    # Got the paddles to move and the ball to bounce regardless of where the paddle is. However:
    # *the ball sticks and the paddle if you move the paddle while close to the ball. , I think it might have to do with the size?*

    if (ball.xcor() < paddle_a.xcor() + 30 and ball.xcor() > paddle_a.xcor() - 20) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 30):
        ball.dx *= -1
        os.system("afplay beep.wav&")

    if (ball.xcor() < paddle_b.xcor() + 30 and ball.xcor() > paddle_b.xcor() - 20) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 30):
        ball.dx *= -1
        os.system("afplay beep.wav&")
