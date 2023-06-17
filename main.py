
import turtle

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
    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 25)

    if shead.direction == "down":
        y = shead.ycor()
        shead.sety(y - 25)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x + 25)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x - 25)

#keyboard bindings
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")


#main game
while True:
    wn.update()





wn.mainloop()