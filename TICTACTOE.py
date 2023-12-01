from random import randrange


# Function will init the Tic Tac Toe board
# for loop to display a number that corresponds with each square for the player to choose from
def init_board():
    global current_player
    board = [['' for x in range(3)] for i in range(3)]
    pos: int = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = pos
            pos += 1

    board[1][1] = 'X'
    current_player = 'O'
    return board


# display the board with the print function by utilizing arguments 'sep' and 'end'
def display_board(board):
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', str(board[row][col]) + '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')


# this function confirms the board's status, prompts the user for a move, then updates the board
def enter_move(board):
    turn_ok = False

    while not turn_ok:
        move = input('Enter a move (1 to 9) : ')

        if len(move) != 1 or move <= '0' or move > '9':
            print("Invalid move, please enter a valid move (enter the number on the Square you wish to choose) ")
            continue

        move = int(move) - 10
        row = move // 3
        col = move % 3

        if board[row][col] in ['O', 'X']:
            print("This Square is taken, please choose another free Square !")
            continue

        turn_ok = not turn_ok
        board[row][col] = 'O'


# Function chooses a move for the computer then updates the board
# This move is chosen from a list of all free squares, these lists contain tuples pair in rows and columns
def free_fields(board):
    free_squares = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free_squares.append((row, column))
    return free_squares


def draw_move(board):
    free_squares = free_fields(board)

    free_squares_length: int = len(free_squares)
    if free_squares_length > 0:
        random = randrange(free_squares_length)
        row, col = free_squares[random]
        board[row][col] = 'X'


# Victory message
# this function checks 3 conditions to determine if Victory
# to determine if Victory the functions checks for a win in the rows, columns, or by diagonal
def victory_for(board, sign):
    # check rows
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return sign

    # check columns
    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return sign

    # check diagonals
    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
            board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return sign

    return None


# Function to start the game
# prompts the user to enter 0 to start or -1 to end the game
def start_the_game():
    game_status = '0'
    while game_status != '-1':
        print('*-----------------------------*')
        print('* Welcome to TicTacToe game!', ' *')
        print('* Enter 0 to start the game.', ' *')
        print('* Enter -1 to end the game.', '  *')
        print('*-----------------------------*')

        game_status = input('Enter your choice : ')

        if type(game_status) != "<class 'str'>" and game_status not in ['0', '-1']:
            print('Please enter 0 or -1')
            continue

        if game_status == '-1':
            break

        # main board checks win or draw
        board = init_board()
        play(board)
        display_board(board)

        if winner != None:
            print()
            print('TIC TAC TOE ! The player', winner, 'got 3 in a row !')
            print()
        else:
            print('Its a Draw !')


def play(board):
    free_squares = len(free_fields(board))
    global winner
    global current_player

    while free_squares != 0:
        display_board(board)

        if current_player == 'O':
            # player turn
            enter_move(board)
        else:
            # computer turn
            draw_move(board)

        winner = victory_for(board, current_player)

        if winner != None:
            winner = winner
            break
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'

        free_squares = len(free_fields(board))


start_the_game()
