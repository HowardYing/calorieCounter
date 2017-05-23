#!/usr/bin/env python3
#created by Addison Richey 4/10/17
def getCal():
    al = [1,1.2,1.375,1.55,1.725,1.9]
    def calcCalM(w,h,a,female,act,wc):
        if female:
            x=10*w+6.25*h-5*a-161
        else:
            x=10*w+6.25*h-5*a+5
        x*= al[act]
        x += wc*1000
        return int(x)
    def calcCalI(w,hf,hi,a,female,act, wc):
        w/=2.20462
        h= ((hf*12)+hi)*2.54
        if female:
            x=10*w+6.25*h-5*a-161
        else:
            x=10*w+6.25*h-5*a+5
        x*= al[act]
        x += wc*500
        return int(x)
    
    m =input("True/False you use the metric system")
    if m:
        a = calcCalM(input("How much do you weigh in kg.?"),input("How tall ar you in cm.?"),input("how many years old are you"),input("True/False you are female."), input("what activity level are you"),input("how many Kg do your weight to chang by each week?"))
        return a
        
    else:
        a= calcCalI(input("How much do you weigh in lbs.?"),input("How tall ft.?"),input("how tall in."),input("how many years old are you"),input("True/False you are female."), input("what activity level are you"),input("how many lbs. do your weight to chang by each week?"))
        return a
