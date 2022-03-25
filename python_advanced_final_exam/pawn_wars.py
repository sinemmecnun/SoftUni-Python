def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def capture_pawn(matrix, row, col, opponent):
    # row + 1, col - 1
    if not is_outside(row + 1, col - 1, 8):
        if matrix[row + 1][col - 1] == opponent:
            return True
    # row + 1, col + 1
    if not is_outside(row + 1, col + 1, 8):
        if matrix[row + 1][col + 1] == opponent:
            return True
    # row - 1, col - 1
    if not is_outside(row - 1, col - 1, 8):
        if matrix[row - 1][col - 1] == opponent:
            return True
    # row - 1, col + 1
    if not is_outside(row - 1, col + 1, 8):
        if matrix[row - 1][col + 1] == opponent:
            return True
    return False

n = 8
board = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0

column_codes = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

game_over = False
promoted = False
winner = ''
queen = ''

for row in range(n):
    data = input().split()
    board.append(data)
    for col in range(n):
        if data[col] == 'b':
            black_row = row
            black_col = col
        elif data[col] == 'w':
            white_row = row
            white_col = col

winner_square = ''
while True:

    if capture_pawn(board, white_row, white_col, 'b'):
        game_over = True
        winner = 'White'
        winner_square += column_codes[black_col] + str(8 - black_row)
        break
    board[white_row][white_col] = '-'
    white_row -= 1
    board[white_row][white_col] = 'w'
    if white_row == 0:
        queen = 'White'
        winner_square += column_codes[white_col] + str(8 - white_row)
        promoted = True
        break

    if capture_pawn(board, black_row, black_col, 'w'):
        winner = 'Black'
        winner_square += column_codes[white_col] + str(8 - white_row)
        game_over = True
        break
    board[black_row][black_col] = '-'
    black_row += 1
    board[black_row][black_col] = 'b'
    if black_row == 7:
        queen = 'Black'
        winner_square += column_codes[black_col] + str(8 - black_row)
        promoted = True
        break


if game_over:
    print(f"Game over! {winner} win, capture on {winner_square}.")
if promoted:
    print(f"Game over! {queen} pawn is promoted to a queen at {winner_square}.")