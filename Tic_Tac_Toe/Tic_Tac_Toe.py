from IPython.display import clear_output
import random


def display_board(board):
    print('                        '+board[7]+'|'+board[8]+'|'+board[9])
    print('                        '+board[4]+'|'+board[5]+'|'+board[6])
    print('                        '+board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    
    while True:
        player1_marker = input('Select your Marker Player1-- X or O: ')
        if player1_marker in ['X', 'O']:
            break
        else:
            print('please select the correct marker')
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker ='X'
    return (player1_marker, player2_marker)

            
def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or (board[1] == board[2] == board[3] == mark) or (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or (board[7] == board[5] == board[3] == mark) or (board[1] == board[5] == board[9] == mark)


def choose_first():
    rand = random.choice(['player1', 'player2'])
    print('Its '+rand+' to play first')
    return rand


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    while True:
        choice = int(input('select the choice (1-9) to place the marker'))
        if choice not in range(1,10):
            print('Provide a valid input')
            continue
        if space_check(board, choice):
            return choice
        else:
            print('Position is not Empty! Try again!')


def replay():
    while True:
        replay = input('Wanna Play Again! "Y" or "N" :')
        if replay in ['Y', 'N', 'n', 'y']:
            break
        else:
            print('Invalid Choice!')
    return replay == ['Y', 'y']


print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()
    player = choose_first()
    if player == 'player1':
        first = 'player1'
        second = 'player2'
        marker1 = player1_marker
        marker2 = player2_marker
    else:
        first = 'player2'
        second = 'player1'
        marker1 = player2_marker
        marker2 = player1_marker
    while True:
        #Player 1 Turn
        display_board(board)
        print(first)
        position = player_choice(board)
        place_marker(board, marker1, position)
        if win_check(board, marker1):
            display_board(board)
            print(player+ ' WON!')
            break
        if full_board_check(board):
            display_board(board)
            print('Board full Draw')
            
        # Player2's turn.
        display_board(board)
        print(second)
        position = player_choice(board)
        place_marker(board, marker2, position)
        if win_check(board, marker2):
            display_board(board)
            print(player+ ' WON!')
            break
        if full_board_check(board):
            display_board(board)
            print('Board full Draw')

    if not replay():
        break

