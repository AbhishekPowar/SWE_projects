import random
def printBoard(board):
    print('\n')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print(f'------------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'------------')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('\n')

def check(board):
    for val in board.values():
        if val == ' ':
            return True
    return False

def win(board):
    winList=[[1,2,3],
                [4,5,6],
                [7,8,9],
                [1,4,7],
                [2,5,8],
                [3,6,9],
                [1,5,9],
                [7,5,3]]
    for part in winList:
        if (board[part[0]] == board[part[1]] == board[part[2]] ) and board[part[0]]!=' ': 
            winner=board[part[0]]
            if winner==userSign:
                print('Congratulation You won')
            elif winner==compSign:
                print('Computer Won')
            else:
                print('Try again later its a TIE')
            return True 

    return False

board={}

for i in range(1,10):
    board.setdefault(i,' ')

compSign='X'
userSign=input("Choose your sign 'X' or 'O' :   ")
    
if userSign in ['X','x']:
    compSign='O'
if userSign in ['0','o','O']:
    compSign='X'

boardValues=set('123456789')

moves=0
while True :
    compPos=int(random.choice(list(boardValues)))
    #compPos=int(input('\nYour move user 1 :   '))
    board[compPos]=compSign
    boardValues-=set(str(compPos))
    printBoard(board)
    moves+=1
    if win(board) or moves==9:
       break

    userPos=int(input('\nYour move user 2 :   '))
    board[userPos]=userSign
    boardValues-=set(str(userPos))
    
    printBoard(board)
    moves+=1

    if win(board) or moves==9:
       break

if moves == 9:
    print("Break")
