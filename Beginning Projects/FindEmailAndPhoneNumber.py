#! python3
#phoneandEmail - finds phone number and email
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
print("Use the findPhoneAndEmail(text) to find E-mail address and phone numbers in text. \nThe function also returns a list of E-mail address and phone numbers in text.")
import re
phoneRegex=re.compile('''
(   \d{3}  |  \( \d{3} \)   )?              #areacode
( \s  |   -    |  \.   )?                   #separator
(  \d{3}  )                                 #first 3 digits
( \s  |   -    |  \.  )?                    #separator
(  \d{4}  )                                 #last 4
''',re.VERBOSE)
emailRegex=re.compile("""
( [w]+ \.)?                   #www.
([a-zA-Z0-9]+)                #username
(@)                           #@ symbol  
([a-zA-Z0-9]+)                #domain name
(\.[a-zA-Z]+)                 #dot-something

""",re.VERBOSE)

def findPhoneAndEmail(text):
    logging.debug('Start of function')
    matches=[]
    for group in phoneRegex.findall(text):
        logging.debug('Phone number found:'+''.join(group))
        phoneNum=' '.join([group[0],group[2],group[4]])
        matches.append(phoneNum)
        print('Phone Number found :' + phoneNum)
    for group in emailRegex.findall(text):
        logging.debug('E=mail found:'+''.join(group))
        email=''.join([group[1],group[2],group[3],group[4]])        
        matches.append(email)
        print('E-mail address found :' + email)
    if len(matches)==0:
        print("No phone numbers or email addresses found.")
    return matches

    
    
        



    
