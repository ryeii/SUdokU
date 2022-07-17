import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

import dancing_link
import mask_solve
import blocked_mask_solve
import back_tracking

quiz_df = pd.read_csv("sudoku_cluewise.csv", sep=',')


def display(board):
    for i in range(9):
        if i in [3, 6]:
            print('------+-------+------')
        for j in range(9):
            if j in [3, 6]:
                print('| ', end='')
            print(board[i * 9 + j] + ' ', end='')
        print()


# In case there is multiple answers for a quiz, here is a function to check whether a solution is valid
def check(sol):
    grid = [sol[i: i + 9] for i in [0, 9, 18, 27, 36, 45, 54, 63, 72]]
    for i in grid:
        if not len(list(set(i))) == 9:
            return False
    for i in range(9):
        l = []
        for j in grid:
            l.append(j[i])
        if not len(list(set(l))) == 9:
            return False
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(grid[i + l][j + k])
            if not len(list(set(block))) == 9:
                return False
    return True


def run_test(m, size):
    correct = []
    solving_time = []
    # plot_clue_size_distribution(quiz_df, size)

    for k in range(len(methods)):
        correct.append(0)
        solving_time.append(0)

        for i in range(size):
            if i % 1000 == 0:
                print("method ", str(k), ': ',str(i), " / ", str(size))
            start = time.time()
            sol = m[k](quiz_df["quizzes"][i])
            end = time.time()
            if quiz_df["solutions"][i] == sol:
                correct[k] += 1
            solving_time[k] += end - start
        solving_time[k] = solving_time[k] / size

    return correct, size, solving_time

display(back_tracking.sol(quiz_df["quizzes"][0]))
print()
display(quiz_df["solutions"][0])

methods = [back_tracking.sol]
correct, size, solving_time = run_test(methods, 1000)
for i in range(len(methods)):
    print("method", str(i), "solved", str(correct[i]), "out of", str(size), "puzzles,", str(correct[i] / size * 100),
          "%. avg solving time: ",
          str(solving_time[i]))
