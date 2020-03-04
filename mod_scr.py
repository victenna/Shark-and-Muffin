#file name: module_scr
import turtle
score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('gold')
s=0
FONT=('Times New Roman',20, 'bold')
def scr():
    global s
    s=s+1
    score.goto(150,250)
    score.clear()           
    score.write ('Score=',font=FONT)
    score.goto(230,250)
    score.write (s,font=FONT)

