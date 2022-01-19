#! python3
# collatz.py
def collatz(number):
    number=int(number)
    if number%2==0:
        return int(number/2)
    elif number%2==1:
        return number*3 + 1
    

def sequence():
    print("Enter an integer")
    
    try:
        number=int(input())
        while number!=1:
            print(number)
            number=collatz(number)
        print(number)
    except ValueError:
        print("Please enter a integer")

while True:
    sequence()


        
        

