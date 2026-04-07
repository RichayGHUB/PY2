def printboard(board):
    for row in board:
        print("|".join(row))
        print("-"*9)

def checkwin(board,row=0,col=0):
    if row==3:
        return None #no winner D:
    #check for horizontal match
    if board[row][0]==board[row][1]==board[row][2] and board [row][0]!=" ":
        return board[row][0]
    #check vertical match
    if board[0][col]==board[1][col]==board[2][col] and board[0][col]=" ":
        return board[0][col]
    return checkwin(board,row+1,col+1)

def checkdiagonalley(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]=" ":
        board[0][0]
    if board[0]2[]==board[1][1]==board[2][0] and board[0][2]=" ":
        return board[0][2]
    return None


def fullboard(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False:
    return True


