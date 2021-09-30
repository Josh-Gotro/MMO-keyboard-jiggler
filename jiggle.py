import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
numMin = None
print("welcome mate")

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1
else:
    numMin = int(sys.argv[1])

while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,2):
        pyautogui.keyDown("w")
        time.sleep(1.1)
        pyautogui.keyUp("w")
        time.sleep(1)
        pyautogui.typewrite("x")

        pyautogui.keyDown("s")
        time.sleep(2)
        pyautogui.keyUp("s")
        time.sleep(1)
        pyautogui.typewrite("x")

    print("Movement made at {}".format(datetime.now().time()))
