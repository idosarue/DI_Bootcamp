theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}


def print_board(board):
    print(board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print('---|-----|---')
    print(board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print('---|-----|---')
    print(board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])


def player_input():
    not_valid = True
    while not_valid:
        square = input("Enter square number: ")
        if not square.isnumeric():
            print('Enter only numbers please..')
        elif square == "0" or square == '10':
            print('Please enter numbers between 1 and 9..')
        else:
            not_valid = False
            return square


def is_game_over(player, counter):
    if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True

    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True


    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
        print(f'player {player} won!')
        print_board(theBoard)
        return True

    if counter == 9:
        print_board(theBoard)
        print('gave over\n it\'s a tie')
        return True
    return False



def play():
    player = "X"
    counter = 0
    for i in range(9):
        print_board(theBoard)
        print(f'It\'s {player}\'s turn')
        move = player_input()
        if theBoard[move] == ' ':
            theBoard[move] = player
            counter += 1
        else:
            print('already filled, try again')
            continue

        if is_game_over(player, counter):
            break

        if player == "X":
            player = "O"
        else:
            player = "X"



play()