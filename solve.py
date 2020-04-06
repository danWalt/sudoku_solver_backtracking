# solve.py is a program which utilizes bruthe force code to solve any
# Sudoku solveable board.

import pprint

# an empty cell is represented by a cell containing the digit 0
EMPTY_CELL = 0

# all possible answers in a Sudoku board
POSSIBLE_ANSWERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# find_empty_cell scans the board for an empty cell and returns it

def find_empty_cell(board):
    for row in range(9):
        for cell_num in range(9):
            if board[row][cell_num] == EMPTY_CELL:
                return row, cell_num
    return None


# makes sure that the new number doesn't appear in the current row
def check_row(board, row, option):
    if option in board[row]:
        return False
    return True


# makes sure that the new number doesn't appear in the current column
def check_column(board, cell_num, option):
    for row in range(9):
        if board[row][cell_num] == option:
            return False
    return True

# the following set of functions check that the current 3X3 box does not
# contain the new number
def top_left(board, row, column, option):
    for i in range(3):
        for j in range(3):
            if board[row + i][column + j] == option:
                return False
    return True


def bot_right(board, row, column, option):
    for i in range(3):
        for j in range(3):
            if board[row - i][column - j] == option:
                return False
    return True


def top_center(board, row, column, option):
    for i in range(3):
        for j in [0, 1, -1]:
            if board[row + i][column + j] == option:
                return False
    return True


def top_right(board, row, column, option):
    for i in range(3):
        for j in range(3):
            if board[row + i][column - j] == option:
                return False
    return True


def center_left(board, row, column, option):
    for i in [0, 1, -1]:
        for j in range(3):
            if board[row + i][column + j] == option:
                return False
    return True


def center_mid(board, row, column, option):
    for i in [0, 1, -1]:
        for j in [0, 1, -1]:
            if board[row + i][column + j] == option:
                return False
    return True


def center_right(board, row, column, option):
    for i in [0, 1, -1]:
        for j in range(3):
            if board[row + i][column - j] == option:
                return False
    return True


def bot_left(board, row, column, option):
    for i in range(3):
        for j in range(3):
            if board[row - i][column + j] == option:
                return False
    return True


def bot_center(board, row, column, option):
    for i in range(3):
        for j in [0, 1, -1]:
            if board[row - i][column + j] == option:
                return False
    return True

# based on the empty cell location, this function calls the relevant
# function to check the 3x3 box.
def check_3x3_box(board, row, column, option):
    row_position = row % 3
    column_position = column % 3
    if row_position == 1 and column_position == 1:
        return center_mid(board, row, column, option)
    elif row_position == 1 and column_position == 2:
        return center_right(board, row, column, option)
    elif row_position == 1 and column_position == 0:
        return center_left(board, row, column, option)
    elif row_position == 2 and column_position == 1:
        return bot_center(board, row, column, option)
    elif row_position == 2 and column_position == 2:
        return bot_right(board, row, column, option)
    elif row_position == 2 and column_position == 0:
        return bot_left(board, row, column, option)
    elif row_position == 0 and column_position == 1:
        return top_center(board, row, column, option)
    elif row_position == 0 and column_position == 2:
        return top_right(board, row, column, option)
    else:
        return top_left(board, row, column, option)


# for each new possible number and a given empty cell if the number fits in
# the empty cell return True. False otherwise
def check_valid_move(board, row, column, option):
    if check_row(board, row, option):
        if check_column(board, column, option):
            if check_3x3_box(board, row, column, option):
                return True
    return False

# does the work, goes over all of the board recursively using bruthe force
# to solve the given sudoku bored
def move(board):
    cell = find_empty_cell(board)
    if cell:
        row, column = cell
    else:
        return True
    for option in POSSIBLE_ANSWERS:
        if check_valid_move(board, row, column, option):
            board[row][column] = option
            if move(board):
                return board
            board[row][column] = EMPTY_CELL
    return False


# Sudoku board example
sudoku_board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]]
b = move(sudoku_board)
pprint.pprint(b)
