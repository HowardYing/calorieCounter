#This class/method (depending on implementation) generates and edits a tiered list of three levels to be exported as save data. IT DOES NOT ACTUALLY SAVE THE OUTPUT YET.
#Each base list is the day, under a week list, under the master list, called allTime.
#This class requires the following: The first three manage the data to be saved: these are the input list that the data will be added to (inputVar), total calories per day (cal), required calories per day (req).
#The last two, "week" and "day", are for identifying which location "cal" and "req" are to be stored within the lists.
#"week" adjusts week number STARTING FROM ZERO, NOT ONE. "wday" adjusts what day of the week "cal" and "req" should be stored as (0-6).
#Note that the class will generate a new list to export to if the inputVar is set to 0. Otherwise, the class will update an existing list if the list is set as inputVar.

import time, pickle
class Save:
    def __init__ (self, inputVar, cal, req, week, wday):
        self.allTime = inputVar
        self.cal = cal
        self.req = req
        self.week = week
        self.wday = wday
        self.checkIfNew()
        
    def checkIfNew(self):
        if self.allTime == 0:
            self.allTime = [[[], [], [], [], [], [], []]]
            self.update()
        else:
            self.update()
            
    def update(self):
        if self.week >= len(self.allTime):
            i = len(self.allTime) - 1
            while i < self.week:
                self.addweek()
                i = i + 1
            self.allTime[self.week][self.wday].append(0)
            self.allTime[self.week][self.wday][0] += self.cal
            self.allTime[self.week][self.wday].extend([self.req])
            self.allTime[self.week][self.wday].append(time.time())
            print self.allTime
        else:
            self.allTime[self.week][self.wday].append(0)
            self.allTime[self.week][self.wday][0] += self.cal
            self.allTime[self.week][self.wday].extend([self.req])
            self.allTime[self.week][self.wday].append(time.time())
            print self.allTime

    def addweek(self):
        self.allTime.append([[] for _ in range(7)])