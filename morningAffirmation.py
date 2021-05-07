from datetime import date
from datetime import datetime
import random
from graphics import *


win = GraphWin("some basic gui examples",800,800)


date = date.today()


weekdays=["Sunday","Monday","Tuesday","Wednesday",
            "Thursday","Friday","Saturday"]
weekday = weekdays[date.weekday()]

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")

quotes = ["Its a small thing to a giant, you got this",
            "Roam wasn't built in a day",
            "Just do it",
            "Do or do not! There is no try",
            "The night is darkess just before the dawn",
            "2nd place is just the 1st loser",
            "Be better than yesterday",
            "Health is wealth",
            "Work hard today for an easy tomorrow",
            "Belive in yourself"
            ]

task = ["Dont forget to make your coffee.",
        "Morinig breath ewww! Brush them teeth!",
        "Iron your cloths",
        "get the kids ready for school",
        "pack lucnh",
        "dont forget breakfast",
        "fruit is best for breakfast",
        "Walk the dog",
        "Dont forget you wallet/purse",
        "Shower!",
        "drink water, hydrate!",
        "Quick 20 mins exercise",
        "Go Shave",
        "Lotion Up",
        "Feed the pets",
        "Water the plants",
        "Check the News",
        "Check weather",
        "Check the traffic"
        ]

line1 = random.choice(quotes)
line2 = "Good Morning today is " + weekday
line3 = date
line4 = "The time is " + currentTime
line5 = random.choice(task)


win.setBackground('orange')
win.getMouse()


t1 = Text(Point(400,80), line1)
t1.setSize(16)
t1.setFace("courier")
t1.setStyle("bold")
t1.setTextColor("black")
t1.draw(win)
win.getMouse()

t2 = Text(Point(400,100), line2)
t2.setSize(16)
t2.setFace("courier")
t2.setStyle("bold")
t2.setTextColor("black")
t2.draw(win)

t2 = Text(Point(400,120), line3)
t2.setSize(16)
t2.setFace("courier")
t2.setStyle("bold")
t2.setTextColor("black")
t2.draw(win)

t2 = Text(Point(400,140), line4)
t2.setSize(16)
t2.setFace("courier")
t2.setStyle("bold")
t2.setTextColor("black")
t2.draw(win)


win.getMouse()

t5 = Text(Point(400,160), line5)
t5.setSize(16)
t5.setFace("courier")
t5.setStyle("bold")
t5.setTextColor("black")
t5.draw(win)
win.getMouse()

win.close()