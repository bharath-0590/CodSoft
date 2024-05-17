import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Function to check for a tie
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to get the best move for the AI
def get_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Function to check if the move is valid
def is_valid_move(board, row, col):
    return board[row][col] == ' '

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, and the AI is O.")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if is_valid_move(board, row, col):
                board[row][col] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        
        print_board(board)

        if check_winner(board) or check_tie(board):
            break

        # AI's turn
        ai_move = get_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
        
        print_board(board)

        if check_winner(board) or check_tie(board):
            break

    winner = check_winner(board)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_game()
