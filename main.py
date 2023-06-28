
import turtle
import math
import random
import time #to add delays
delay = 0.2


#awaiting updates
#snake size
snake_length = 1

#main window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("grey")
wn.setup(width=800, height=800)
wn.tracer(0)  #No snake is seen at the begining

#game borders
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-400, -400)
border_pen.pendown()
border_pen.pensize(20)
for side in range(4):
    border_pen.fd(800)
    border_pen.lt(90)
border_pen.hideturtle()


#score label
score = 0
high_score = 0

#score display
def display_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()  #to hide the turtle
    pen.goto(0, 300)
    pen.write("Score: " + str(score) +" High Score: " + str(high_score), align="center", font=("Helvetica", 24, "bold"))
    return pen
    
def display_game_over():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()  #to hide the turtle
    pen.goto(0, 0)
    pen.write("Game Over\n Start Again", align="center", font=("Helvetica", 24, "bold"))
    return pen


#the head
shead = turtle.Turtle()
shead.shape('square')
shead.color('green')
shead.speed(0)
shead.penup()  #Snake moves without leaving ink behind
shead.goto(0, 0)
shead.direction = "stop"

sbody = []   #snake's body which will grow

#fns
def move_up():
    if shead.direction != "down":
        shead.direction = "up"

def move_down():
    if shead.direction != "up":
        shead.direction = "down"

def move_left():
    if shead.direction != "right":
        shead.direction = "left"

def move_right():
    if shead.direction != "left":
        shead.direction = "right"

def move():
    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 20)

    if shead.direction == "down":
        y = shead.ycor()
        shead.sety(y - 20)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x - 20)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

#create the food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.speed(0)
food.penup()
food.goto(0, 100)

#main game

scoreboard = display_score()

while True:
    
    wn.update()
    #if you touch the sides game over
    if shead.xcor() > 390 or shead.xcor() < -390 or shead.ycor() > 390 or shead.ycor() < -390:
        time.sleep(1)
        shead.goto(0, 0)
        shead.direction = "stop"

        #hide the body
        for body in sbody:
            body.goto(1000, 1000)

        lost = display_game_over()
        wn.update()
        time.sleep(1)
        #clear the body list
        sbody.clear()

        #reset the score
        score = 0
        scoreboard.clear()
        scoreboard = display_score()
        delay = 0.2
        lost.clear()
        wn.update()


    if shead.distance(food) < 20:  #eat the food
        x = random.randint(-395, 395)
        y = random.randint(-395, 395)
        food.goto(x, y)
        score += 10
        if score > high_score:
            high_score = score
        scoreboard.clear()
        scoreboard = display_score()

        # adding to body
        add_body = turtle.Turtle()
        add_body.speed(0)
        add_body.shape("square")
        add_body.color("green")
        add_body.penup()
        sbody.append(add_body)

        delay -= 0.002

    for i in range(len(sbody)-1, 0, -1):
        x = sbody[i - 1].xcor()
        y = sbody[i - 1].ycor()
        sbody[i].goto(x, y)

    if len(sbody) > 0:
        x = shead.xcor()
        y = shead.ycor()
        sbody[0].goto(x, y)

    move()
    time.sleep(delay)


wn.mainloop()