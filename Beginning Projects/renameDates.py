#! python3
#renameDates.py - Renames filenames with mm-dd-yyyy format into dd-mm-yyyy format
import shutil, os,re
 #create regex to match mm-dd-yyyy format
datePattern=re.compile(r'''
^(.*)                     #all text before the date
((0|1)?\d)               #one or twon digits for month
((0|1|2|3)?\d)           #on or two digits for day
((19|20)\d\d)            #four digits for the year
(.*)$                    #all text after the date

''',re.VERBOSE)

trialPattern=re.compile(r'^(.*)(.*)$')
 #Look over the files in the working directory
for file in os.listdir('.'):
     
    mo=datePattern.search(file)
    tr=trialPattern.search(file)


    #Skip files without a date
    if mo==None:
        
        continue
    
    #Get the different parts of the filename
    before=mo.group(1)
    month=mo.group(2)
    day=mo.group(4)
    year=mo.group(6)
    after=mo.group(8)
    euroFile=before+day+'-'+month+'-'+year
    extraFile=tr.group(1)+str(int(tr.group(2))+1000)
    #Get the full absolute file paths
    absWorkingDir=os.path.abspath('.')
    file=os.path.abspath(absWorkingDir,file)
    eurofile=os.path.abspath(absWorkingDir,euroFile)
    print('MOCK:Renaming "%s" to "%s".....'%(file,euroFile))
    print('MOCK:Renaming "%s" to "%s".....'%(file,extraFile))
     
     
