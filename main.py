import random


EMPTY_SPACE = '-'


def print_board(board):
    # row by row
    for i in range(1, 8, 3):
        print( f'{board[i]}\t{board[i+1]}\t{board[i+2]}' )
        print()


def read_number(command):
    while True:
        num = input(command)
        if not num.isdigit():
            print('Must be a number')
        else:
            num = int(num)
            if num not in range(1, 10):
                print('Must be between 1 and 9')
            else:
                return num


def read_coordinates(board):
    position = None
    while True:
        position = read_number('Where will you place your mark (1-9)? ')
        if board[position] == EMPTY_SPACE:
            break
        else:
            print('Space occupied')
    return position


def verify_win(board, mark):
    # primary diagonal
    if board[1] == board[5] == board[9] == mark:
        return True
    # secondary diagonal
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        # columns
        for i in range(1, 4):
            if board[i] == board[i+3] == board[i+6] == mark:
                return True
        # rows
        for i in range(1, 8, 3):
            if board[i] == board[i+1] == board[i+2] == mark:
                return True
        return False


def verify_tie(board):
    return EMPTY_SPACE not in board


def play_game(players):
    board = [None] + [EMPTY_SPACE]*9
    random.shuffle(players)
    done = False
    while not done:
        for player in players:
            print_board(board)
            print(f"<< {player['name']} >>")
            position = read_coordinates(board)
            board[position] = player['mark']
            print('------------------------------------')
            if verify_win(board, player['mark']):
                print_board(board)
                print( f"Winner: {player['name']}" )
                print('Congratulations!!!')
                done = True
                break
            elif verify_tie(board):
                print_board(board)
                print('There was a tie')
                done = True
                break


print('  _   _        _               _             ')
print(' | | (_)      | |             | |            ')
print(' | |_ _  ___  | |_ __ _  ___  | |_ ___   ___ ')
print(' | __| |/ __| | __/ _` |/ __| | __/ _ \ / _ \\')
print(' | |_| | (__  | || (_| | (__  | || (_) |  __/')
print('  \__|_|\___|  \__\__,_|\___|  \__\___/ \___|')
print()
print('Board layout:')
print()
print_board( [None] + list(range(1, 10)) )

players = []

# reading player id
for i in range(1, 3):
    print(f'<< Player {i} >>')
    name = input('Name: ')
    mark = None
    while True:
        mark = input('Mark: ')
        if len(mark) > 1:
            print('Please enter just one character')
        elif mark in (EMPTY_SPACE, '_'):
            print('Invalid mark')
        else:
            break
    players.append( {'name': name, 'mark': mark} )

print('------------------------------------')

continue_playing = True

while continue_playing:
    play_game(players)

    print('------------------------------------')

    while True:
        option = input('Continue playing (y/n)? ')
        if option in ('y', 'n'):
            break
        else:
            print('Invalid option!')
    if option == 'n':
        break
