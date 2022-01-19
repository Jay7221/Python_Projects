#! python3
# Caser.py

std_str = 'abcdefghijklmnopqrstuvwxyz'

def EncryptLetter(letter, n):
    '''Encrypts a single letter'''
    for i in range(len(std_str)):
        if letter in std_str:
            ind = std_str.index(letter)
            if ind >= len(std_str):
                ind -= len(std_str)
            return std_str[ind]
    return letter
    
    
    
    
def encrypt():
    n = input()
    input_str = input()
    output_str = ''
    for i in range(len(input_str)):
        output_str += EncryptLetter(input_str[i], n)
    print(output_str)
    return output_str

encrypt()
        
        
        
