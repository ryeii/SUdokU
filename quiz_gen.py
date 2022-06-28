from random import sample
import pandas as pd

base  = 3
side  = base*base


# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s,len(s)) 


def gen_solution(base):
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return board


def gen_quiz(base, empties):
    temp = gen_solution(base)
    board = temp.copy()
    sol = ''.join(''.join(''.join(str(j)) for j in temp[i]) for i in range(9))
    squares = side*side
    for p in sample(range(squares), empties):
        board[p//side][p%side] = 0
    return (''.join(''.join(''.join(str(j)) for j in board[i]) for i in range(9)), sol)

print(gen_quiz(base, 64))

data_frame = [["quizzes", "solutions", "clue_numbers"]]
pd.DataFrame(data_frame).to_csv("sudoku_cluewise.csv", sep=',', index=False, header=False)

data_frame = []
counter = 0
for i in range(1, 65):
    print(i)
    for j in range(1000):
        quiz, sol = gen_quiz(base, i)
        data_frame.append([quiz, sol, 81 - i])
        counter += 1
        if counter == 44200:
            df = pd.DataFrame(data_frame)
            df.to_csv("sudoku_cluewise1.csv", sep=',', index=False, header=False)
            with open('sudoku_cluewise.csv', 'a') as outfile:
                with open('sudoku_cluewise1.csv') as infile:
                    for line in infile:
                        outfile.write(line)
            data_frame = []
            counter = 0
df = pd.DataFrame(data_frame)
df.to_csv("sudoku_cluewise1.csv", sep=',', index=False, header=False)
with open('sudoku_cluewise.csv', 'a') as outfile:
    with open('sudoku_cluewise1.csv') as infile:
        for line in infile:
            outfile.write(line)
