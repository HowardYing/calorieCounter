#Ask Kapptie about the non-permanant scene changes
#Make code more Efficient

from Calendar import Calendar
from Button import Button

def setup():
    size(800,300)
    pg = createGraphics(40,40)
    #ask about pg
    global page 
    page = 0                                
button1=Button(100,150,133,80,255,230,180,"Calendar",135,197)
button2=Button(333,150,134,80,255,230,180,"Todays Calories",345,197)
button3=Button(567,150,133,80,255,230,180,"Setup",610,197)
button4=Button(20,20,60,40,255,230,180,"Exit",35,45)
button5=Button(720,20,60,40,255,230,180,"Back",735,45)
calendar=Calendar

def draw():
    # Main Screen 
    background(230,245,115)
    global page
    if page == 0:
        textSize(26)
        text("Calorie Calculator",300,50)
        textSize(15)
        
        button1.display()    
        #will launch Calendar mnu
            
        button2.display()
        #will launch Todays Calories menu
        
        button3.display()
        #will launch Setup menu
        
        button4.display()
    if button4.click==True:
        exit()
                
    if button1.click == True:
        page = 1
    if page==1:
        calendar.display
        '''
        clear()
        background(116, 131, 155)
        textSize(26)
        text("Calendar",340,50)
        textSize(15)
        button5.display()
    '''
        if button5.click == True:
            page = 0
    if button2.click == True:
        page = 2
    if page==2:
    
        clear()
        background(100,244,130)
        textSize(26)
        text("Todays Calories",310,50)
        textSize(15)
        button5.display()
   
        if button5.click == True:
            page = 0
    if button3.click == True:
        page = 3
    if page==3:
   
        clear()
        background(244,100,100)
        textSize(26)
        text("Setup",355,50)
        textSize(15)
        button5.display()
  
        if button5.click == True:
            page = 0
    if button5.click == True:
        page = 0
        