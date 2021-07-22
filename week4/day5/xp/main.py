theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
board_keys = []

for key in theBoard:
    board_keys.append(key)

def print_board(board):
    print(board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print('---|-----|---')
    print(board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print('---|-----|---')
    print(board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])


def player_input():
    square = input("Enter square number: ")
    return square


def play():
    player = "X"
    counter = 0
    for i in range(10):
        print_board(theBoard)
        print(f'It\'s {player}\'s turn')
        move = player_input()
        if theBoard[move] == ' ':
            theBoard[move] = player
            counter += 1
        else:
            print('already filled, try again')
            continue

        if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break

        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
            print(f'player {player} won!')
            print_board(theBoard)
            break
        if counter == 9:
            print('gave over\n it\'s a tie')


        if player == "X":
            player = "O"
        else:
            player = "X"




play()
