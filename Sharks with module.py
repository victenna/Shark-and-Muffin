# File name: Sharks_Muffin

import turtle,random,time
from mod_muffin import muffin
from mod_scr import scr      #import module score
from mod_shark import shapes 
from mod_shark import sprite

import winsound # Import sound library
wn=turtle.Screen()
wn.setup(700,700)
wn.bgpic('Aquarium.gif')
im=[]
shapes(im)
print(im)
shark=turtle.Turtle()
sprite(shark,im[0])
shark.goto(0,-200)
muffin1=turtle.Turtle()
muffin(muffin1)

def right():
    sprite(shark,im[0])
    shark.fd(10)
    
def left():
    sprite(shark,im[1])
    shark.fd(-10)
    
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
        
    delta=abs(shark.position()-muffin1.position())
    
    if delta <50:
        muffin1.hideturtle()
        frequency=1000 #Sound
        duration=100  # Sound
        winsound.Beep(frequency,duration) # Sound
        #print(delta1)
        muffin1.goto(random.randrange(-300,300),300)
        scr()
        time.sleep(0.1)

    
    
    
