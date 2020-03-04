# File name: Sharks_Muffin

import turtle,random,time
import module_scr       #import module score
from module_shark import sharkk0     #import module shark
from module_shark import sharkk1 
import module_muffin    #import module muffin 
import winsound # Import sound library
wn=turtle.Screen()
wn.setup(700,700)
wn.bgpic('Aquarium.gif')


shark1=turtle.Turtle()
shark2=turtle.Turtle()


sharkk0(shark1)
sharkk1(shark2)

shark1.showturtle()
shark2.hideturtle()

muffin1=turtle.Turtle()
module_muffin.muffin(muffin1)

def right():
    shark2.hideturtle()
    shark1.showturtle()
    shark1.fd(10)
    X1=shark1.xcor()
    shark2.setx(X1)

def left():
    shark1.hideturtle()
    shark2.showturtle()
    shark2.fd(-10)
    X2=shark2.xcor()
    shark1.setx(X2)

wn.onkey(left,"Left")
wn.onkey(right, "Right")
wn.listen()
delta1=1000
turtle.tracer(1)
while True:
    muffin1.fd(10)
    if muffin1.ycor()<-300:
        muffin1.hideturtle()
        muffin1.goto(random.randrange(-300,300),300)
        muffin1.showturtle()
        
    delta1=abs(shark1.position()-muffin1.position())
    
    if delta1 <50:
        muffin1.hideturtle()
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound
        print(delta1)
        muffin1.goto(random.randrange(-300,300),300)
        module_scr.scr()
        time.sleep(0.1)

    
    
    
