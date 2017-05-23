#Addison, due to limitations in my knowledge, we have to settle with this display class. All this does is give a specific entry from the nested "allTime" list.
#The class requires three variables: the huge nested list from the calInputClass, which will be unpacked.
#The week number, starting from 0, and the weekday number (0-6).
#The class outputs two things: eCal (the recorded number of calories eaten for that specific day), and rCal (the required amount of calories for that day)
#The GUI for the display will have to be different. The user will have to input a specific week and day, and the program will return the required calories and recorded calories for that day.
import time, pickle
class Load:
    def __init__ (self, allTime, week, wday):
        self.allTime = allTime
        self.week = week
        self.wday = wday
        self.unpack()
    
    def unpack (self):
        eCal = self.allTime[self.week][self.wday][0]
        rCal = self.allTime[self.week][self.wday][1]
        print self.allTime
        print eCal, rCal