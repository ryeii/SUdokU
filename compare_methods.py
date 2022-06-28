import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

import dancing_link
import mask_solve
import blocked_mask_solve

quiz_df = pd.read_csv("sudoku.csv", sep=',')
print(quiz_df.size)


def display(board):
    for i in range(9):
        if i in [3, 6]:
            print('------+-------+------')
        for j in range(9):
            if j in [3, 6]:
                print('| ', end='')
            print(board[i * 9 + j] + ' ', end='')
        print()


def plot_clue_size_distribution(quiz_df, size):
    plt.figure(figsize=(5, 5))
    plt.title("Clue size distribution")
    plt.xlabel("Clue size")
    plt.ylabel("Number of quizzes")
    clue_size = []
    for i in range(size):
        clue_size.append(81 - quiz_df["quizzes"][i].count('0'))
    plt.hist(clue_size, bins=range(10, 60, 10))
    plt.show()


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

# display(blocked_mask_solve.solve(quiz_df["quizzes"][0]))
# print()
# display(quiz_df["solutions"][0])

methods = [mask_solve.solve, blocked_mask_solve.solve, dancing_link.sol]
correct, size, solving_time = run_test(methods, 2000)
for i in range(len(methods)):
    print("method", str(i), "solved", str(correct[i]), "out of", str(size), "puzzles,", str(correct[i] / size * 100),
          "%. avg solving time: ",
          str(solving_time[i]))
