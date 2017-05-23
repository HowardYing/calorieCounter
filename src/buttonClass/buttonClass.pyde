#This sample code creates a single button and causes the background to change color if clicked.
from Button import Button
def setup():
    size(500,500)

button1=Button(50,50,80,60,"test",210,128,80)
def draw():
    button1.display()
    if button1.click == True:
        background(200,128,212)
        button1.display()
    else:
        background(210)
        button1.display()
    