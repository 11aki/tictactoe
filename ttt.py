import sys
board = []  #initd board 
value ='x' #whose turn is it x/y
turns = 0  # how many turns have been played
xo = True   # change from x's turn to o's and vice versa
drawn = [] #positions already drawn at
#change the value in the board
def changeVal(pos):
    global value
    global turns
    xx = int((pos/3))
    yy = int(pos%3-1)
    if(pos%3==0):
        xx = xx-1
    print("changed value")
    board[xx][yy] = value
    turns += 1
    displayBoard(board)
    checkWin()
    xTurn()
    askUser()

def checkWin():
    global turns
    global board
    global value
    v= True
    diagonalLR = True
    diagonalRL = True
    
    if turns>3:
        #chec horizontal
        for row in board:
            if len(set(row)) == 1:
                print(value+" won the game in row ")
                resetGame()
        #check vertical
        for i in range(3):
            for j in range(len(board)-1):
                #print(board[j+1][i])
                if board[j][i]!=board[j+1][i]:
                    v= False
            if v== True:
                print(value+" won the game in column "+str(i+1))
                resetGame()
            v = True
        #check diagonal left to right
        for i in range(len(board)-1):
            if board[i][i]!=board[i+1][i+1]:
                diagonalLR = False
        #check diagonal right to left
            if board[len(board)-i-1][i] != board[len(board)-i-2][i+1]:
                diagonalRL = False
        if diagonalLR or diagonalRL :
            print(value+" won the game in diagonal ")
            resetGame()
        #if diagonalRL : print(value+" won the game in diagonal Right to Left ")

    if turns == 9:
        print("tie game")
        resetGame()

#change x to o
def xTurn():
    global xo
    global value
    xo = not xo
    if xo == False:
        value = 'o'
    else: value = 'x'


#display the current board
def displayBoard(board):
    for x in board:
        print(*x,sep = " ")


#askUser which position to input his value
def askUser():
    global value
    global drawn
    print("Its {}'s turn, Enter which pos to draw".format(value))
    posi =int(input())
    if drawn.count(posi)== 1:
        print("That spot is already taken, try again")
        askUser()
    else: 
        drawn.append(posi)
        print("added")
    changeVal(posi)

#resetGame and ask to play again
def resetGame():
    global board
    global value
    global turns
    global xo
    inp =''
    inp = input("do u wanna start a game? 1 to start  ")
    if inp=='1':
        board = [[1,2,3],[4,5,6],[7,8,9]]
        value ='x'
        turns = 0
        xo = True
        displayBoard(board)
        askUser()
    else:
        print("Goodbye!")
        sys.exit()

resetGame()
