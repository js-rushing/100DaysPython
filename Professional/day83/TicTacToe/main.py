import os

line = '-------------'
l = '| '
r = ' |'
m = ' | '
top = [' ', ' ', ' ']
mid = [' ', ' ', ' ']
bot = [' ', ' ', ' ']
placements = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

current_player = 1
game_over = False
game_result = {
    "winner": 0,
    "win_line": (0, 0)
}


def clear_console():
    clear = 'clear'
    if os.name in ('nt', 'dos'):
        clear = 'cls'
    os.system(clear)


def get_row(row_list):
    return '| ' + row_list[0] + ' | ' + row_list[1] + ' | ' + row_list[2] + ' |'


def display_scheme():
    print('The squares are numbered thusly.')
    print(line)
    print('| 1 | 2 | 3 |')
    print(line)
    print('| 4 | 5 | 6 |')
    print(line)
    print('| 7 | 8 | 9 |')
    print(line)


def display_board_two():
    print(line)
    print(l + placements[0] + m + placements[1] + m + placements[2] + r)
    print(line)
    print(l + placements[3] + m + placements[4] + m + placements[5] + r)
    print(line)
    print(l + placements[6] + m + placements[7] + m + placements[8] + r)
    print(line)


def get_square_choice():
    global current_player
    choice = int(input('Player {}, pick a square:'.format(current_player)))
    if current_player == 1:
        placements[choice - 1] = 'X'
        current_player = 2
    elif current_player == 2:
        placements[choice - 1] = 'O'
        current_player = 1


def play_round():
    global game_over
    get_square_choice()
    clear_console()
    display_board_two()
    if board_is_full() or game_is_won():
        game_over = True
    # Figure out if game is over or not


def board_is_full():
    for sq in placements:
        if sq == ' ':
            return False
    return True


def set_result(square, win_line):
    global game_result

    winner = 0

    if square == 'X':
        winner = 1
    else:
        winner = 2

    game_result = {
        "winner": winner,
        "win_line": win_line
    }


def game_is_won():
    global game_result
    if placements[0] != ' ':
        # If top row win
        if placements[0] == placements[1] and placements[0] == placements[2]:
            set_result(placements[0], (0, 2))
            return True
        # If left col win
        if placements[0] == placements[3] and placements[0] == placements[6]:
            set_result(placements[0], (0, 6))
            return True
        # If l-r diagonal win
        if placements[0] == placements[4] and placements[0] == placements[8]:
            set_result(placements[0], (0, 8))
            return True
    if placements[4] != ' ':
        # If mid row win
        if placements[3] == placements[4] and placements[3] == placements[5]:
            set_result(placements[4], (3, 5))
            return True
        # If mid col win
        if placements[1] == placements[4] and placements[1] == placements[7]:
            set_result(placements[4], (1, 7))
            return True
        # If r-l diagonal win
        if placements[6] == placements[4] and placements[6] == placements[2]:
            set_result(placements[4], (6, 2))
            return True
    if placements[8] != ' ':
        # If bot row win
        if placements[6] == placements[7] and placements[6] == placements[8]:
            set_result(placements[8], (6, 8))
            return True
        # If right col win
        if placements[2] == placements[5] and placements[2] == placements[8]:
            set_result(placements[8], (2, 8))
            return True
    return False


print('This is  Tic Tac Toe')
display_scheme()

while not game_over:
    play_round()

if game_over:
    print('Game Over')
if game_result["winner"] != 0:
    print('Player {} Wins!'.format(game_result["winner"]))
else:
    print('No winner this time.')
