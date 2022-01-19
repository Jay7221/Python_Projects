import os,re
print('Please enter the path of the folder you wish to search:')
folder=input()
print('Please enter the regular expression you wish to search:')
regex=input()
ouput=[]
for file in os.listdir(folder):
    matches=regex.findall(file)
    for match in matches:
        output .append(match)

print(output)
