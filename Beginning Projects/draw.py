#! python3
# draw.py - draws a spiral square
print('You have 10 seconds before system takes control!')
import pyautogui,time
time.sleep(10)
pyautogui.click()
from pyautogui import dragRel
distance=300
while distance>0:
    dragRel(distance,0,duration=0.001) #move right
    distance=distance - 5
    dragRel(0,distance,duration=0.001) #move down
    distance=distance - 5
    dragRel(-distance,0,duration=0.001) #move left
    distance=distance - 5
    dragRel(0,-distance,duration=0.0015) #move up
    distance=distance - 5
