# Define the board as a 2D array of strings
board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["r", "n", "b", "q", "k", "b", "n", "r"]]

# Define a function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Define a function to get the legal moves for a piece at a given location
def get_legal_moves(board, row, col):
    legal_moves = []
    piece = board[row][col]
    if piece == "P":
        if row == 1 and board[row+1][col] == " " and board[row+2][col] == " ":
            legal_moves.append((row+2, col))
        if row < 7 and board[row+1][col] == " ":
            legal_moves.append((row+1, col))
        if col > 0 and row < 7 and board[row+1][col-1].islower():
            legal_moves.append((row+1, col-1))
        if col < 7 and row < 7 and board[row+1][col+1].islower():
            legal_moves.append((row+1, col+1))
    elif piece == "R":
        for i in range(row+1, 8):
            if board[i][col] == " ":
                legal_moves.append((i, col))
            else:
                if board[i][col].islower():
                    legal_moves.append((i, col))
                break
        for i in range(row-1, -1, -1):
            if board[i][col] == " ":
                legal_moves.append((i, col))
            else:
                if board[i][col].islower():
                    legal_moves.append((i, col))
                break
        for j in range(col+1, 8):
            if board[row][j] == " ":
                legal_moves.append((row, j))
            else:
                if board[row][j].islower():
                    legal_moves.append((row, j))
                break
        for j in range(col-1, -1, -1):
            if board[row][j] == " ":
                legal_moves.append((row, j))
            else:
                if board[row][j].islower():
                    legal_moves.append
