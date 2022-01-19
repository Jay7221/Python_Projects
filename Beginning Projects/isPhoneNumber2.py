import re
def isPhoneNumber(text):
    phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    mo=phoneNumRegex.search(text)
    if mo!=None:
        print('Phone number found:' + mo.group())
        print(' Area code:'+ mo.group(1))
    else:
        print("No phone number found.")
         
         


print("Use the function isPhoneNumber() to find out if given text has a phone number of format ddd-ddd-dddd")


