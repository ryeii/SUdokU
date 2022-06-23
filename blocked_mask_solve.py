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


def to_str(mat):
    return ''.join(''.join(str(mat.tolist()[i])) for i in range(9))

