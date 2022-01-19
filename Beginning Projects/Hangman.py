import random
HANGMANPICS=["""
    +------------+
    |            |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
                 |
                 |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
    |            |
                 |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
   /|            |
                 |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
   /|\           |
                 |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
   /|\           |
   /             |
                 |
                 |
                 |
                 |
====================


""","""
    +------------+
    |            |
    O            |
   /|\           |
   / \           |
                 |
                 |
                 |
                 |
====================


"""]
words={"pets":"""
    Dog
    Puppy
    Turtle
    Rabbit
    Parrot
    Cat
    Kitten
    Goldfish
    Mouse
    Tropical fish
    Hamster

""".split(),"farm animals":"""
    Cow
    Rabbit
    Ducks
    Shrimp
    Pig
    Goat
    Crab
    Deer
    Bee
    Sheep
    Fish
    Turkey
    Dove
    Chicken
    Horse
""".split(),"birds":"""
    Crow
    Peacock
    Dove
    Sparrow
    Goose
    Stork
    Pigeon
    Turkey
    Hawk
    Bald eagle
    Raven
    Parrot
    Flamingo
    Seagull
    Ostrich
    Swallow
    Black bird
    Penguin
    Robin
    Swan
    Owl
    Woodpecker
""".split()}
def getRandomWord(wordDict):
    #This function returns a random string from the passed list of strings
    wordKey=random.choice(list(wordDict.keys()))
    wordIndex=random.randint(0,len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex],wordKey]


def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print("Missed Letters:", end="")
    for letter in missedLetters:
        print (letter+" ", end="")
    print()
    blanks="_"*len(secretWord)
    for i in range(len(secretWord)):
        #Replace blanks with correctly guessed words
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    for letter in blanks:
        #Show the secret word with space in between each letter
        print(letter+" ",end="")
    print()

def getGuess(alreadyGuessed):
    #returns the letter player entered.This function makes sure the player entered a single letter, and not something else.
    while True:
        print("Guess a letter.")
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter.Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        else:
            return guess
def playAgain():
    #this function returns True if the player wants to play again, otherwise it returns False.
    print("Do you want to play again.(Yes or No)")
    return input().lower().startswith("y")
print("HANGMAN")
missedLetters=""
correctLetters=""
secretWord,secretKey=getRandomWord(words)
gameIsDone=False
print("The secret key is "+secretKey)

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    #Lets the player type in a letter
    guess=getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters=correctLetters + guess
        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes!The secret word is " + secretWord + ".You have won.")
            break
            
    else:
        missedLetters = missedLetters + guess
        #Check if player has guessed too many times and lost
        if len(missedLetters)==len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print("You have run out of guesses!\nAfter "+str(len(missedLetters))+" missed guesses and "+str(len(correctLetters))+" correct guesses, the word was "+secretWord+".")
            gameIsDone=True
    if gameIsDone:
         if playAgain():
             missedLetters=""
             correctLetters=""
             gameIsDone=False
             secretWord=getRandomWord(words)
         else:
            break
                 
