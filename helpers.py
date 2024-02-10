def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
            
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'
def check_for_win(spots):
    # Check rows for a win
    for i in range(1, 8, 3):
        if spots[i] == spots[i + 1] == spots[i + 2] != ' ':
            return True

    # Check columns for a win
    for i in range(1, 4):
        if spots[i] == spots[i + 3] == spots[i + 6] != ' ':
            return True

    # Check diagonals for a win
    if (spots[1] == spots[5] == spots[9] != ' ') or (spots[3] == spots[5] == spots[7] != ' '):
        return True

    # If no win condition is met
    return False
