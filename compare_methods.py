import pandas as pd
import time

import dancing_link
import mask_solve

quiz_df = pd.read_csv("sudoku.csv", sep=',')


def display(board):
    for i in range(9):
        if i in [3, 6]:
            print('------+-------+------')
        for j in range(9):
            if j in [3, 6]:
                print('| ', end='')
            print(board[i * 9 + j] + ' ', end='')
        print()


def run_test(m):
    correct = []
    solving_time = []
    size = 500

    for k in range(len(methods)):
        correct.append(0)
        solving_time.append(0)

        for i in range(size):
            if i % 1000 == 0:
                print(str(i), " / ", str(size))
            start = time.time()
            sol = m[k](quiz_df["quizzes"][i])
            end = time.time()
            if quiz_df["solutions"][i] == sol:
                correct[k] += 1
            solving_time[k] += end - start
        solving_time[k] = solving_time[k] / size

    return correct, size, solving_time


# display(systematic_solve.solve(quiz_df["quizzes"][0]))
# print()
# display(quiz_df["solutions"][0])

methods = [mask_solve.solve, dancing_link.sol]
correct, size, solving_time = run_test(methods)
for i in range(len(methods)):
    print("method", str(i), "solved", str(correct[i]), "out of", str(size), "puzzles,", str(correct[i] / size * 100),
          "%. avg solving time: ",
          str(solving_time[i]))
