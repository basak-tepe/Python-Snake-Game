import turtle
import math


win = True
time_left = True


# Create a screen
screen = turtle.Screen()
screen.title("Cake Delivery Game")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)



# End game displays as a list
# 0 win
# 1 lose by time
# 2 lose by error
end_game_options = ["Congratulations, you delivered the cake on time!",
            "Failed successfully. You ran out of time and the cake has gone bad!",
            "Failed successfully. You got crashed by a car!"]


#Characters
characters = ["Burçak","Başak","Elif","Jane", "İrem", "Jack", "Jill", "James", "İlknur", "Jade", "Yigit", "Jasmine", "Jared", "Jocelyn", "Jude", "Jules", "Cengiz", "Juliet", "Julia", "Işıl"]


#win / lose display
def end_game_display(end_game_options):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)

    if win: #win
        end_game_option = end_game_options[0]
    elif time_left: #lose by crash
        end_game_option = end_game_options[2]
    else: #lose by time
        end_game_option = end_game_options[1]

    pen.write(end_game_option, align="center", font=("Courier", 24, "normal"))


#the sidewalks
def draw_sidewalks():
    return 0



# Create cake of diameter 20
cake = turtle.Turtle()
cake.speed(0)
cake.shape("circle")
cake.color("pink")
cake.penup()
cake.goto(0, 0)
cake.direction = "stop"
screen.update()

#moving the cake with arrow keys
# Moving the cake
def move_up():
    y = cake.ycor()
    y += 20
    cake.sety(y)
    screen.update()

def move_down():
    y = cake.ycor()
    y -= 20
    cake.sety(y)
    screen.update()

def move_left():
    x = cake.xcor()
    x -= 20
    cake.setx(x)
    screen.update()

def move_right():
    x = cake.xcor()
    x += 20
    cake.setx(x)
    screen.update()


# Bind arrow keys to movement functions
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()
turtle.done()