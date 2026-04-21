def printboard(board):
    for row in board:
        print("|".join(row))
        print("-"*9)
"""""
def checkwin(board,row=0,col=0):
    if row==3:
        return None #no winner D:
    #check for horizontal match
    if board[row][0]==board[row][1]==board[row][2] and board [row][0]!=" ":
        return board[row][0]
    #check vertical match
    if board[0][col]==board[1][col]==board[2][col] and board[0][col]!=" ": 
        return board[0][col]
    return checkwin(board,row+1,col+1)
"""
def checkwin(board, row=0, col=0):
    """
    Check for a winner using recursion.
    - Checks rows and columns by incrementing indices recursively.
    - Stops when a winner is found or all rows/columns are checked.
    """
    # Base case: if we've checked all rows and columns
    if row == 3:
        return None  # No winner found

    # Check current row
    if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
        return board[row][0]

    # Check current column
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
        return board[0][col]

    # Recursively check the next row and column
    return checkwin(board, row + 1, col + 1)
def checkdiagonalley(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!=" ":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=" ":
        return board[0][2]
    return None


def fullboard(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
def playgame():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    current_player = "X"

    while True:
        printboard(board)
        print("It's {} turn!".format(current_player))

        row = (int(input("Input ROW 1-3: ")))-1
        column = (int(input("Input COLUMN 1-3: ")))-1

        if board[row][column] == " ":
            board[row][column] = current_player
        else:
            print("Cell already taken! Try again.")
            continue
        #check a winner
        winner = checkwin(board) or checkdiagonalley(board)
        if winner:
            printboard(board)
            print("{} WINS! GG!".format(winner))
            break
        


            #DRAW
        if fullboard(board):
            printboard(board)
            print("DRAW :(")
            break

        #switch players
        current_player = "O" if current_player=="X" else "X"

playgame()
