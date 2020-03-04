#file name: module_muffin
import turtle
wn=turtle.Screen()
image0='muffin1.gif'

def muffin(turtle):
    wn.addshape(image0)
    turtle.shape(image0)
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(-90)
    turtle.goto(0,300)
    turtle.showturtle()
    
 
    

