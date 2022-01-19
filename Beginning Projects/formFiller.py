#! python3
# formFiller - Automatically fills in the form.

import pyautogui,time

nameField=(404,394)
submitButton=(394,641)
submitButtonColor=(130,184,223)
submitAnotherLink=(440,233)
delay=0.1
formData=[{'name':'Alice','fear':'eavesdroppers','source':'wand','robocop':4,'comments':'Tell Bob I said hi.'},
          {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,'comments': 'n/a'},
          {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball','robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
          {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money','robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]



for person in formData:
    print('>>>>GIVING USER 5 SECONDS TO PRESS CTRL-C<<<<<')
    time.sleep(5)

    #wait while the form page has loaded.
    #while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        #time.sleep(1)

    print('Entering %s info ......'%(person['name']))
    pyautogui.click(nameField[0],nameField[1])
    pyautogui.typewrite(person['name']+'\t',delay)
    pyautogui.typewrite(person['fear']+'\t',delay)

    #Fill out the Source of Wizard Powers field.
    if person['source']=='wand':
        pyautogui.typewrite(['down','enter','\t'],delay)
    elif person['source']=='amulet':
        pyautogui.typewrite(['down','down','enter','\t'],delay)
    elif person['source']=='crystal ball':
        pyautogui.typewrite(['down','down','down','enter','\t'],delay)
    elif person['source']=='money':
        pyautogui.typewrite(['down','down','down','down','enter','\t'],delay)

    #Fill out the RoboCop field.
    if person['robocop']==1:
        pyautogui.typewrite(['right','left','\t','\t'],delay)
    elif person['robocop']==2:
        pyautogui.typewrite(['right','\t','\t'],delay)
    elif person['robocop']==3:
        pyautogui.typewrite(['right','right','\t','\t'],delay)
    elif person['robocop']==4:
        pyautogui.typewrite(['right','right','right','\t','\t'],delay)
    elif person['robocop']==5:
        pyautogui.typewrite(['right','right','right','right','\t','\t'],delay)

    #Fill out Additional Comments field.
    pyautogui.typewrite(person['comments'],delay)
    pyautogui.typewrite(['\t'],delay)

    #Click Submit.
    pyautogui.typewrite(['enter'],delay)

    #Wait until form page has loaded.
    print('Clicked Submit')
    time.sleep(5)

    #Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])
    

    
    

    
    

    
    
