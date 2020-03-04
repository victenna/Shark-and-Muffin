#file name: mod_shark
import turtle
wn=turtle.Screen()


def shapes(im):
    for m in range(2):
        im.append('shark'+str(m+1)+'.gif')
        
def sprite(turtle,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    



