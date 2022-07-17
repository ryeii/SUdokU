import numpy as np
import time
import back_tracking

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
    return [[item for sublist in l for item in sublist] for l in sub_grids]


# Reverse the effect of to_sub_grids.
def to_quiz(sub_grids):
    quiz = ''
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    quiz += str(sub_grids[i*3+k][j*3+l])
    return quiz


# Takes a 9x9 matrix "mask" and a pair of coordinates (i, j) and returns a 9x9 matrix "mask" with the masking applied.
def masking(mask, i, j):
    for k in range(9):
        mask[i][k] = 1
    for k in range(3):
        mask[i % 3 + k * 3][j % 3] = 1
        mask[i % 3 + k * 3][j % 3 + 3] = 1
        mask[i % 3 + k * 3][j % 3 + 6] = 1
    for k in range(3):
        mask[i // 3 * 3 + k][j // 3 * 3] = 1
        mask[i // 3 * 3 + k][j // 3 * 3 + 1] = 1
        mask[i // 3 * 3 + k][j // 3 * 3 + 2] = 1
    return mask


# Takes a string of 81 characters representing a board and returns a string of 81 characters representing the solved board.
def solve(quiz):
    sub_grids = np.array(to_sub_grids(quiz))
    nums_not_done = []
    for i in range(1, 10):
        r, _ = np.where(sub_grids == i)
        if len(r) < 9:
            nums_not_done.append(i)
    start = time.time()
    while nums_not_done and time.time() - start < 0.0006:
        for k in nums_not_done:
            mask = sub_grids.copy()
            r, c = np.where(mask == k) 
            for i in range(len(r)):
                mask = masking(mask, r[i], c[i])
            for i in range(9):
                list = mask[i].tolist()
                if list.count(0) == 1:
                    sub_grids[i, list.index(0)] = k
                    r, _ = np.where(sub_grids == k)
                    if len(r) == 9:
                        nums_not_done.remove(k)
    if nums_not_done:
        return back_tracking.sol(to_quiz(sub_grids))

    return to_quiz(sub_grids)



