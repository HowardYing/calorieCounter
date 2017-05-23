from button import Button
global s1
s1 = 1
def setup():
    size(200,200)
    global p
    p=1
b1 = Button(1,1,50,50,0,100,200)
b2 = Button(100,100,50,50,0,100,200)
import json
def draw():
    global s1, p
    if s1:
        b1.display()
        b2.display()
        if b1.click:
            p = 1
            s1 = 0
        elif b2.click:
            p = 0 
            s1 = 0    
    else:
        if p:    
            with open("result.json", 'w') as fp:
                json.dump(123456789, fp)
        jsonData = open('result.json')
        with open('result.json') as fp:
            x = json.load(jsonData)
        print x