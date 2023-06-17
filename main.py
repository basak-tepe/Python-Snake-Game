
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
wn.bgcolor("gray")
wn.setup(width=800, height=800)
wn.tracer(0)  #No snake is seen at the begining

#the head
shead = turtle.Turtle()
shead.shape('square')
shead.color('black')
shead.speed(0)
shead.penup()  #Snake moves without leaving ink behind
shead.goto(0, 0)
shead.direction = "stop"

#fns
def move_up():
    shead.direction = "up"

def move_down():
    shead.direction = "down"

def move_left():
    shead.direction = "left"

def move_right():
    shead.direction = "right"

def move():
    consume_food()
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

global food
global food_exists #food presence
food_exists = False

#generate food on the screen
#random coordinates each time
def generate_food():
    global food_exists
    global food
    if food_exists == False:
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        food = turtle.Turtle()
        food.shape('circle')
        food.color('red')
        food.speed(0)
        food.penup()
        food.goto(x, y)
        food_exists = True
        return food
    else:
        return None

def consume_food():
    global food_exists
    global food
    global snake_length
    if shead.distance(food) < 20:
        #we should have used clear
        food.hideturtle()
        snake_length += 1
        food_exists = False
        return True
    else:
        return False

#main game
while True:
    wn.update()
    generate_food()
    move()
    time.sleep(delay)





wn.mainloop()