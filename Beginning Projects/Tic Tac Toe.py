#! python3
#Tic Tac Toe
import random
def drawBoard(board):
    #This functions prints out the board that it was passed.
    #'board' is a list of 10 strings representing the board.
    print("    |    |")
    print("  "+board[7]+" |  "+board[8]+" | "+board[9])
    print("    |    |")
    print("------------------")
    print("    |    |")
    print("  "+board[4]+" |  "+board[5]+" | "+board[6])
    print("    |    |")
    print("------------------")
    print("    |    |")
    print("  "+board[1]+" |  "+board[2]+" | "+board[3])
    print("    |    |")

def inputPlayerLetter():
    #Let's player type which letter they want to be
    #Returns a list with the player's letter as the first item, and the computer's letter as the second item.
    letter=""
    while not (letter=="X"or letter=="O"):
        print("Do you want to play as X or O")
        letter=input().upper()
        #the first letter in te list is the player's letter, the second letter is the computer's letter.
    if letter=="X":
        return["X","O"]
    else:
        return["O","X"]

def whoGoesFirst():
    #Randomly choose the player who goes first.
    if random.randint(0,1)==0:
        return "computer"
    else:
        return "player"

def playAgain():
    #This function returns True if the player wants to play again, otherwise it returns false.
    print("Do you want to play again(Yes or No)")
    return input().lower().startswith("y")

def makeMove(board, letter, move):
    board[move]=letter

def isWinner(board,letter):
    #Given a board and a player's letter, this function returns True if that player has won.
    def isInLine(x,y,z):
        return board[x]==board[y]==board[z]==letter
    return isInLine(1,2,3)or isInLine(4,5,6)or isInLine(7,8,9)or isInLine(1,4,7)or isInLine(2,5,8)or isInLine(3,6,9)or isInLine(1,5,9)or isInLine(3,5,7)
def getBoardCopy(board):
    #Make a duplicate of the board list and return it the duplicate.
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,move):
    #Returns true if the passed move is free on the passed board.
    return board[move]==" "

def getPlayerMove(board):
    #Let the player type in his move.
    move=""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board,int(move)):
        print("What is your next move?(1-9)")
        move=input()
    return int(move)

def chooseRandomMoveFromList(board,moveList):
    #Retuens a valid move from the passed list on the passed board.
    possibleMoves=[]
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter=="O":
        playerLetter="X"
    else:
        playerLetter="O"

    #Here is our algorithm for Tic Tac Toe AI:
    #First, check if we can win in the next move.
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    #Check if the player could win on his next move, block them.
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #Try to take one of the corners, if any are free.
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move!= None:
        return move

    #Try to take the center, if it is free.
    if isSpaceFree(board,5):
        return 5

    #Move on one of the sides.
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #Returns True if every space on the board has been taken.
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print("Welcome to Tic Tac Toe !!")

while True:
    #Reset the board.
    board=[" "]*10
    stdBoard=['','1','2','3','4','5','6','7','8','9']
    playerLetter,computerLetter=inputPlayerLetter()
    turn=whoGoesFirst()
    print("The "+ turn + " will go first.")
    gameIsPlaying=True

    while gameIsPlaying:
        if turn== "player":
            #Player's turn
            drawBoard(stdBoard)
            print()
            print()
            drawBoard(board)
            move=getPlayerMove(board)
            makeMove(board, playerLetter, move)

            if isWinner(board, playerLetter):
                drawBoard(board)
                print("Hooray! You have won the game!")
                gameIsPlaying=False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print("The game is a tie!")
                    break
                else:
                    turn="computer"
        else:
            #computer's turn
            move=getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)
            if isWinner(board, computerLetter):
                drawBoard(board)
                print("The computer has beaten you! You lose.")
                gameIsPlaying=False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print("The game is a tie!")
                    break
                else:
                    turn="player"
    if not playAgain():
        break

