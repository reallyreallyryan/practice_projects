# Trying Pong Tutorial to learn Python
# Tutorial from freecodeacademy

# Part 1: Getting Started

import turtle #turtle module allows for graphics and is built it no need to install
import os

wn = turtle.Screen() #this is the window
wn.title("Pong Python Tutorial")
wn.bgcolor('black') #this is the background color
wn.setup(width=800, height=600) #this is the size of the window
wn.tracer(0) #this stops window from updating -> have to manually updated it, makes the game faster


# Score
score_a = 0 #variables to start with
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # every time it moves it moves 2 pixels
ball.dy = 2

# Pen -> writing on screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #this is so we dont draw a line when the pen moves, if we dont do pen up, there will be a line on sceen
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function -> a piece of program that does something that was defined for it
def paddle_a_up(): #have to def what the function is to start
    y = paddle_a.ycor() # from turtle module, it returns the y coords
    y += 20 #adds pixels to y coord
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keybord Binding
wn.listen() #tells computer to listen for computer input in window -> only need one
wn.onkeypress(paddle_a_up, "w") #says "when user presses W call the function paddle a up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #this is for the arrow keys
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop -> this is where the main part of the games go to
while True:
    wn.update() #every time loop runs it updates the screen

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking -> what happens when the ball hits the border
    if ball.ycor() > 290:
        ball.sety(290) #avoids problems?
        ball.dy *= -1 #reverses the direction of the ball
        os.system("afplay 268156__thirteenthfail__beat.wav&") #'afplay' is for mac; the "&" makes it not stop when playing sound

    if ball.ycor() < -290:
        ball.sety(-290) #avoids problems?
        ball.dy *= -1
        os.system("afplay 268156__thirteenthfail__beat.wav&")

    if ball.xcor() > 390: #ball is off the screen -> to score
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #clears previous numbers
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: #ball is off the screen -> to score
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay 268156__thirteenthfail__beat.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay 268156__thirteenthfail__beat.wav&")