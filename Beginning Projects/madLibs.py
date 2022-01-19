#! python3
#MadLibs.py - Lets user create new file with ADJECTIVE , NOUN and VERB substituted by words of their choice
import re,shutil
print('Enter file to be change:')
userInput=input()
print('Enter an adjective:')
adjectiveSub=input()
print('Enter an noun:')
nounSub=input()
print('Enter an verb:')
verbSub=input()

file=open(userInput,'r')
fileData=file.read()
file.close
regex1=re.compile('ADJECTIVE')
regex2=re.compile('NOUN')
regex3=re.compile('VERB')
newFile=regex1.sub(adjectiveSub,fileData)
newFile=regex2.sub(nounSub,newFile)
newFile=regex3.sub(verbSub,newFile)
print(newFile)
file=open(userInput,'w')
file.write(newFile)
file.close()
