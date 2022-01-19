#! python3
#mcb.py - saves and loads pieces of text to clipboard
print('''
save <keyword> - saves keyword to clipboard
<keyword> - Loads keyword to clipboard
list - loads all krywords to clipboard
''')

import shelve, pyperclip, sys
mcbShelf=shelve.open('mcb')

#Save clipboard Content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mubShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    #List keywords and load contents
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])






mcbShelf.close()
