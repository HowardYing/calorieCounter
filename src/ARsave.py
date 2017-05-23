#!/usr/bin/env python3
#created Addison Richey 4/12/17
import pickle
from dailyCalories import getCal
o = input("True/False this is your first time opening this program. ")
if o:
    with open('savefile','w') as f:
        pickle.dump(getCal(),f)
with open('savefile') as f:
    x = pickle.load(f)

print x
