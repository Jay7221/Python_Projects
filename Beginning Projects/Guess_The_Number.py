import random
guessestaken=0
print("HELLO! What is your name")
myname=input().title()

number=random.randint(1,20)

print("Well, " + myname + ", I am thinking of a number between 1 and 20")

while guessestaken<6:
    print("Take a guess")
    guess=input()
    guess=int(guess)

    guessestaken=guessestaken+1

    if guess<number:
        print("Your guess is too low")
    if guess>number:
        print("Your guess is too high")
    if guess==number:
       break
if guess==number:
    guessestaken=str(guessestaken)
    print("Good Job, "+myname+"! You have guessed my number in "+guessestaken+" gusses.")
if guess!=number:
    number=str(number)
    print("Nope. The number I was thinking of was "+number+".")
