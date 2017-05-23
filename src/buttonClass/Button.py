#This button class requires 8 variables to function. 
#In order: the xcoord, ycoord, width, height, text, nonhover color (c1), hover color(c2), and click color (c3).
#There is a boolean, "click", which you can call on for click detection and execution.

class Button:
    def __init__ (self, x, y, w, h, t, c1, c2, c3):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.t=t
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.over=False
        self.click=False
        
    def display (self):
        self.mouse()
        self.hover()
        if self.over == True:
            if self.click ==True:
                fill(self.c3)
                rect(self.x, self.y, self.w, self.h, 4)
                fill(0)
                text(self.t, self.x+12, self.y+20) #Adjust text offset here. Offsets must match.
            else:
                fill(self.c2)
                rect(self.x, self.y, self.w, self.h, 4)
                fill(0)
                text(self.t, self.x+12, self.y+20) #Adjust text offset here. Offsets must match.
        else:
            fill(self.c1)
            rect(self.x, self.y, self.w, self.h, 4)
            fill(0)
            text(self.t, self.x+12, self.y+20) #Adjust text offset here. Offsets must match.
    
    def hover (self):
        if mouseX > self.x and mouseX < self.x+self.w and mouseY > self.y and mouseY < self.y+self.h:
            self.over=True
        else:
            self.over=False
            
    def mouse (self):
        if mousePressed == True and self.over == True:
            self.click=True
        else:
            self.click=False