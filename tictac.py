# Initialize the board as a dictionary with positions 1 to 9
board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

# Symbols for player and computer
player = 'X'
computer = 'O'

# Function to print the board
def print_board(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# Function to check if someone has won
def check_win(board, mark):
    # Define winning combinations
    win_combinations = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # columns
        ['1', '5', '9'], ['3', '5', '7']  # diagonals
    ]
    
    # Check if any winning combination is filled with the same mark
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    # Iterate over each position on the board
    for position in board.values():
        # If any position is still empty, return False (not a draw)
        if position == ' ':
            return False
    # If no empty positions were found, return True (it's a draw)
    return True


# Minimax algorithm to determine the best move
def minimax(board, is_maximizing):
    if check_win(board, computer):
        return 1
    if check_win(board, player):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')  # Initialize to negative infinity
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '  # Undo the move
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')  # Initialize to positive infinity
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '  # Undo the move
                best_score = min(best_score, score)
        return best_score

# Function to make the computer's move
def computer_move():
    best_score = -float('inf')
    best_move = None

    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                best_move = key

    if best_move is not None:
        board[best_move] = computer

# Function to handle the player's move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move in board.keys() and board[move] == ' ':
            board[move] = player
            break
        else:
            print("Invalid move. Please try again.")

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        player_move()
        print_board(board)
        if check_win(board, player):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Computer's turn
        computer_move()
        print("Computer's move:")
        print_board(board)
        if check_win(board, computer):
            print("Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
