import numpy as np
import time
import back_tracking


def display(board):
    for i in range(9):
        if i in [3, 6]:
            print('------+-------+------')
        for j in range(9):
            if j in [3, 6]:
                print('| ', end='')
            print(board[i * 9 + j] + ' ', end='')
        print()


def to_mat(quiz):
    return np.array([[int(quiz[i * 9 + j]) for j in range(9)] for i in range(9)])


def to_str(mat):
    return ''.join(''.join(str(mat[i][j]) for j in range(9)) for i in range(9))


def masking(mask, i, j):
    for t in range(9):
        mask[i][t] = 1
        mask[t][j] = 1
    for t in range(3):
        mask[i // 3 * 3][j // 3 * 3 + t] = 1
        mask[i // 3 * 3 + 1][j // 3 * 3 + t] = 1
        mask[i // 3 * 3 + 2][j // 3 * 3 + t] = 1
    return mask


def secondary_masking(mask):
    rows, cols = np.where(mask == 0)
    block_wise = [[] for _ in range(9)]
    for i in range(len(rows)):
        block_wise[rows[i] // 3 * 3 + (cols[i] // 3)].append([rows[i], cols[i]])
    for i in range(9):
        if len(block_wise[i]) in [2, 3]:
            if all(v[0] == block_wise[i][0][0] for v in block_wise[i]):
                for t in range(9):
                    mask[block_wise[i][0][0]][t] = 1
                for t in block_wise[i]:
                    mask[block_wise[i][0][0]][t[1]] = 0
            elif all(v[1] == block_wise[i][0][1] for v in block_wise[i]):
                for t in range(9):
                    mask[t][block_wise[i][0][1]] = 1
                for t in block_wise[i]:
                    mask[t[0]][block_wise[i][0][1]] = 0
    return mask


def critical(mask, i, j):
    block_wise = []
    for t in range(3):
        block_wise.append(mask[i // 3 * 3][j // 3 * 3 + t])
        block_wise.append(mask[i // 3 * 3 + 1][j // 3 * 3 + t])
        block_wise.append(mask[i // 3 * 3 + 2][j // 3 * 3 + t])
    return block_wise.count(0) == 1


def solve(quiz):
    mat = to_mat(quiz)
    nums_not_done = []
    for i in range(1, 10):
        r, _ = np.where(mat == i)
        if len(r) < 9:
            nums_not_done.append(i)
    start = time.time()
    while nums_not_done and time.time() - start < 0.0006:
        for k in nums_not_done:
            mask = np.copy(mat)
            rows, cols = np.where(mat == k)
            for i in range(len(rows)):
                mask = masking(mask, rows[i], cols[i])
            mask = secondary_masking(mask)
            rows, cols = np.where(mask == 0)
            for i in range(len(rows)):
                if critical(mask, rows[i], cols[i]):
                    mat[rows[i], cols[i]] = k
                    r, _ = np.where(mat == k)
                    if len(r) == 9:
                        nums_not_done.remove(k)
    ans = ''
    for i in mat.tolist():
        for j in i:
            ans += str(j)
    if nums_not_done:
        return back_tracking.sol(ans)
    return ans

