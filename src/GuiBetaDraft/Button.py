#This button class requires 7 variables to function. 
#In order: the xcoord, ycoord, width, height, nonhover color (c1), hover color(c2), and click color (c3).
#There is a boolean, "click", which you can call on for click detection and execution.
#TH EDIT- added text (t), text xcoord (tx) and text ycoord (ty) to variables to bring the total variables to 10. This will allow for greater customization of each button as needed.


class Button:
    def __init__ (self, x, y, w, h, c1, c2, c3, t, tx, ty):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.t=t
        self.tx=tx
        self.ty=ty
        self.over=False
        self.click=False
        
    def display (self):
        x=self.x
        y=self.y
        w=self.w
        h=self.h
        t=self.t
        tx=self.tx
        ty=self.ty
        self.mouse()
        self.hover()
        if self.over == True:
            if self.click ==True:
                fill(self.c3)
                rect(x, y, w, h, 4)
                fill(0)
                text(t, tx, ty) #Adjust text offset here. Offsets must match.
            else:
                fill(self.c2)
                rect(x, y, w, h, 4)
                fill(0)
                text(t, tx, ty) #Adjust text offset here. Offsets must match.
        else:
            fill(self.c1)
            rect(x, y, w, h, 4)
            fill(0)
            text(t, tx, ty) #Adjust text offset here. Offsets must match.
    
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