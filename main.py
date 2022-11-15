import random

EMPTY_SPACE = '-'


def print_board(board):
    for row in board:
        print( f'{row[0]}\t{row[1]}\t{row[2]}' )
        print()


def read_number(command):
    while True:
        num = input(command)
        if not num.isdigit():
            print('Must be a number')
        elif num not in ('1', '2', '3'):
            print('Must be between 1 and 3')
        else:
            return int(num) - 1


def read_coordinates(board, player):
    while True:
        line = read_number('Line (1-3): ')
        column = read_number('Column (1-3): ')
        if board[line][column] in ('-', '_'):
            break
        else:
            print('Space occupied')

    return line, column


def verify_win(board, symbol):
    # main diagonal
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    # other diagonal
    elif board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    # first column
    elif board[0][0] == board[1][0] == board[2][0] == symbol:
        return True
    # second column
    elif board[0][1] == board[1][1] == board[2][1] == symbol:
        return True
    # third column
    elif board[0][2] == board[1][2] == board[2][2] == symbol:
        return True
    # rows
    else:
        for row in board:
            if row[0] == row[1] == row[2] == symbol:
                return True
        else:
            return False


def verify_tie(board):
    tie = True
    for row in board:
        if EMPTY_SPACE in row:
            tie = False
            break
    return tie


def play_game(players):
    board = ( [EMPTY_SPACE]*3, [EMPTY_SPACE]*3, [EMPTY_SPACE]*3 )
    random.shuffle(players)
    done = False
    while not done:
        for player in players:
            print_board(board)
            print(f"<< {player['name']} >>")
            line, column = read_coordinates(board, player)
            board[line][column] = player['symbol']
            print('------------------------------------')
            if verify_win(board, player['symbol']):
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

players = []

# reading player id
for i in range(1, 3):
    print(f'<< Player {i} >>')
    name = input('Name: ')
    symbol = None
    while True:
        symbol = input('Symbol: ')
        if len(symbol) > 1:
            print('Please enter just one symbol')
        elif symbol == EMPTY_SPACE:
            print('Invalid symbol')
        else:
            break
    players.append( {'name': name, 'symbol': symbol} )

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
