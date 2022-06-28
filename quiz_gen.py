from random import sample

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


def gen_quiz(sol):
    board = sol
    squares = side*side
    empties = squares * 3 // 4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    numSize = len(str(side))
    for line in board:
        print(*(f"{n or '.':{numSize}} " for n in line))


gen_quiz(gen_solution(base))
