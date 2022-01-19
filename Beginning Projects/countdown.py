#! python3
#countdown.py - A simple countdown script

import time , subprocess

timeleft=60
while timeleft>0:
    print(timeleft,end='....')
    time.sleep(1)
    timeleft=timeleft-1

