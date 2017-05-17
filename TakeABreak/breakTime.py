# breakTime.py
# written by michael Zarate

import time
import webbrowser

breakNum = 0

print("This program has started on: " + time.ctime())
while breakNum < 3:
    time.sleep(5)
    webbrowser.open("https://youtu.be/8UqUrRnh0XI")
    breakNum += 1
