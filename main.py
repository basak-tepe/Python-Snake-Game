
import turtle

#main window

mw = turtle.Screen()
mw.title("Snake Game")
mw.bgcolor("gray")
mw.setup(width=800, height=800)


#the snake
snake = turtle.Turtle()
snake.shape('square')
snake.color('black')
snake.speed(0)
snake.goto(100, 100)








mw.mainloop()