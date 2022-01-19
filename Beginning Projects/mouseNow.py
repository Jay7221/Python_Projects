#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
def mouseNow():
    print('Press CTRL-C to quit.')
    try:
        while True:
            x,y=pyautogui.position()
            pixelColor=pyautogui.screenshot().getpixel((x,y))
            positionStr='X: '+str(x).rjust(4)+'Y: '+str(y).rjust(4)
            positionStr=positionStr+'RGB:  '+str(pixelColor)
            print(positionStr,end='')
            print('\b'*len(positionStr),end='',flush=True)
    except KeyboardInterrupt:
        print('\nDone')

    



    
                
        
        



    
