#global variables
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
game_ongoing = True
winner = None
current_player = 'O'

#functions
def play_game():
    display_board()
    while game_ongoing:
        handle_turn(current_player)
        check_game_over()
        flip_player()
    if winner == 'X' or winner == 'O':
        print(winner + ' won')
    else:
        print('Tie')

def display_board():
    for idx, space in enumerate(board): 
        if idx % 3 == 0:
            print(f'{board[idx]} | {board[idx+1]} | {board[idx+2]}\n')

def handle_turn(mark):
    print(f'{mark}\'s turn')
    while True:
        position = input('Choose a position from 1 to 9: ')
        if not position.isdigit() or not (1 <= int(position) <= 9):
            print('Invalid input. Please try again')
        else:
            position = int(position) - 1
            if(board[position]!='-'):
                print('Someone has already taken that space. Please try again')
            else:
                board[position] = mark
                break

    display_board()

def check_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_ongoing

    for idx, space in enumerate(board):
        if idx % 3 == 0:
            if (board[idx] == board[idx+1] == board[idx+2]) and space != '-':
                game_ongoing = False
                return space
    return

def check_columns():
    global game_ongoing

    for idx in range(0,3):
        if idx % 3 == 0:
            if (board[idx] == board[idx+3] == board[idx+6]) and board[idx] != '-':
                game_ongoing = False
                return board[idx]
    return

def check_diagonals():
    global game_ongoing

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    if diagonal_1 or diagonal_2:
        game_ongoing = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_tie():
    global game_ongoing

    if '-' not in board:
        game_ongoing = False
    return

def flip_player():
    global current_player
    
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

play_game()

