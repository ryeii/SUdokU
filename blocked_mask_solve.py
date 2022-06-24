import numpy as np


def display(board_str):
    board_str = to_str(board_str)
    for i in range(9):
        if i in [3, 6]:
            print('------+-------+------')
        for j in range(9):
            if j in [3, 6]:
                print('| ', end='')
            print(board_str[i * 9 + j] + ' ', end='')
        print()


def to_mat(quiz):
    return np.array([[int(quiz[i * 9 + j]) for j in range(9)] for i in range(9)])


# Takes a string of 81 characters and returns a list of 9x9 matrices, each representing a 3x3 sub-grid.
def to_sub_grids(quiz):
    mat = to_mat(quiz)
    sub_grids = []
    for i in range(9):
        for j in range(9):
            if i in [0, 3, 6]:
                if j in [0, 3, 6]:
                    sub_grids.append(mat[i:i + 3, j:j + 3])
    return sub_grids

# Takes a list of 9x9 matrices and returns a string of 81 characters, representing the board.
def to_quiz(sub_grids):
    quiz = ''
    for i in range(9):
        for j in range(9):
            quiz += str(sub_grids[i][j].tolist()[0])
    return quiz


