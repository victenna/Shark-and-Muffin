#file name: module_shark
import turtle
wn=turtle.Screen()
image=['shark1.gif','shark2.gif']


def sharkk0(turtle):
    wn.addshape(image[0])
    turtle.shape(image[0])
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,-200)
    turtle.showturtle()

def sharkk1(turtle):
    wn.addshape(image[1])
    turtle.shape(image[1])
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,-200)
    turtle.showturtle()
   


