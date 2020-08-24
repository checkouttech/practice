# Welcome to your Samba TV interview, Kapil.  My name is Allen and I will
# be working with you on a small coding challenge today.
#
# Challenge:
#
#   Implement a simple tic-tac-toe game
#
# Requirements:
#
#  1. program must play a game for both players with no user interaction
#     - program does not have to choose player moves intelligently
#  2. program must display the game board after each player move
#     - just print to stdout
#     - don't bother drawing the lines making up the board grid, just
#       display the board as three characters on three lines.
#     - display player tokens with 'x' and 'o', empty spaces with a '.'
#
#       An example board in initial state would display:
#
#          ...
#          ...
#          ...
#
#       After a few moves, the board might display as:
#
#          ..x
#          o.x
#          ..o
#
#  3. program must display the game winner if won, or 'draw' if not won
#
# Begin when ready, and remember to verbalize your design and implementation
# thoughts as you proceed.  I'm as interested in understanding your problem-
# solving process, and the rationale behind your design choices, as much as
# I am in you demonstrating your ability to implement your solution.
#




# gameMatrix  = ['.', '.','.','.','.', '.','.', '.', '.']

gameBoard  = ['X', '.','.','O','.', 'O','.', 'X', 'X']


winLines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),    
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)]


def displayGameBoard (gameBoard) :
        
    print "".join(gameBoard[0:3])
    print "".join(gameBoard[3:6])
    print "".join(gameBoard[6:9])


def checkIfWin(gameBoard, playerID) :
    
    # using any combined with map function 
    if any row  matches
    if any column matches
    if either diagnol matches 
    
    
    
def playAMove(gameBoard, playerID) :
    
    validMoveAvailable =  [ i for i in range(9) if gameBoard[i] == '.']
    

    if ( len(validMoveAvailable) == 0 ) :
        return "No valid moves available " 
    
    
    from random import randint    
        
    moveIndex =    randint(0,len(validMoveAvailable)-1) 
    
    movePostion = validMoveAvailable[moveIndex]
     
        
    print "valid moves available ", validMoveAvailable
    

    
    print "playing move ", movePostion
    
    if ( playerID == 1 ) :
        gameBoard[movePostion] =  "X" 
        print "playing player 1 " 
    elif ( playerID == 2 ) : 
        gameBoard[movePostion] =  "O"     

        
        
    checkIfWin(gameBoard, playerID) 
    
    return gameBoard


    
    
    
    '''
    # Pick up a random 
    
    validMove = False 
    while (not validMove) : 
        
        # pick random value 
        # check if value is taken 
    

    return gameMatrix 
'''

displayGameBoard(gameBoard) 
print""    
gameBoard = playAMove(gameBoard,1)
print"" 
displayGameBoard(gameBoard) 
print"" 
gameBoard = playAMove(gameBoard,2)
print"" 
displayGameBoard(gameBoard) 

    
    
    
'''
for i in range (9) 

    # Get input from random-1 
    # Display updated game board 
    # Check if its a win if yes then output result and exit 
    
    # check if valid moves remaining
    
    # Get input from random-2 
    # Display updated game board 

    # check if its a win  if yes then output result and exit 
    
    
    
'''    









