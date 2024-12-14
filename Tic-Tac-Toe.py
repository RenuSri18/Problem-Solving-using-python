def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    for turn in range(9):
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        print_board(board)
        x, y = map(int, input("Enter row and column (0-2): ").split())
        if board[x][y] == " ":
            board[x][y] = player
            if check_winner(board, player):
                print(f"Player {player} wins!")
                print_board(board)
                return
        else:
            print("Invalid move. Try again.")
    print("It's a draw!")
    print_board(board)

tic_tac_toe()
