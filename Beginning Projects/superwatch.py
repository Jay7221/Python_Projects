#! python3
#superwatch.py - A simple stopwatch
import time
print('Press ENTER to begin. Afterwaeds, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
input()
print('Started')
startTime=time.time()
lastTime=startTime
lapNum=1

try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print(('Lap #'+ '%s'.rjust(5)+ ':' '%s'.rjust(5)+'(%s)'.rjust(5))%(lapNum,totalTime,lapTime),end='')
        lapNum=lapNum+1
        lastTime=time.time()

except KeyboardInterrupt:
    print('\n DONE')
    
