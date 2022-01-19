import random
import sys

def drawBoard(board):
    #draw the board data structure
    hline="   " #initial space for the numbers down the left side of the board.
    for i in range(1,5):
        hline=hline + (" "*9) + str(i)

    # print the numbers across the top
    print(hline)
    print("   " + ("0123456789"*6))
    print()

    # print each of the 15 rows
    for i in range(15):
        # single-digit ni=umbers need to be padded with an extra space
        if i<10:
            extraSpace=" "
        else:
            extraSpace=""
        print("%s%s %s %s"%(extraSpace , i getRow(board,i), i))

    # prints numbers across the bottom
    print()
    print("   " + ("0123456789"*6))
    print(hline)

def getBoard(board , row):
    # returns a string from the board data structure at a certain row.
    boardRow=""
    for i in range(60):
        boardRow += board[i][row]
    return boardRow
    
def getNewBoard():
    #Create a new 60x15 board data structure.
    board=[]
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==o:
                board[x].append("~")
            else:
                board[x].append("`")
    return board

def getRandomChests(numChests):
    chests=[]
    for i in range(numChests):
        chests.append([randeom.randint(59),random.randint(0,14)])
    return chests

def isValidMove(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def makeMove(board, chests , x ,y):
    if not isValidMove(x , y):
        return False
    smallestDistance = 100
    for cx , cy in chests:
        if abs(cx - x)>abs(cy - y):
            distance=abs(cx - x)
        else:
            distance=abs(cy - y)
        if distance <= smallestDistance:
            smallestDistance = distance
            
