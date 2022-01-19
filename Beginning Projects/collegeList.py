#! python3
#collegeList.py
import os
print('ENTER FILENAME')
filename=input()
fileObj=open(filename)
fileData=fileObj.read()
lines=[]
for line in fileData.split('\n'):
    lis=line.split()
    if lis[-4]=='OPEN':
        print(line)
        lines.append(line)
data='\n'.join(lines)
file=open(os.path.join('C:/Users/School Projects/Desktop','select'+os.path.basename(filename)),'w')
file.write(data)
file.close()
        
    
