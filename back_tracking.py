# A Backtracking program 
# in Python to solve Sudoku problem

import numpy as np
import time

# Function to Find the entry in 
# the Grid that is still not used
# Searches the grid to find an 
# entry that is still unassigned. If
# found, the reference parameters 
# row, col will be set the location
# that is unassigned, and true is 
# returned. If no unassigned entries
# remains, false is returned.
# 'l' is a list variable that has 
# been passed from the solve_sudoku function
# to keep track of incrementation 
# of Rows and Columns
def find_empty_location(arr, l):
	for row in range(9):
		for col in range(9):
			if(arr[row][col]== 0):
				l[0]= row
				l[1]= col
				return True
	return False

# Returns a boolean which indicates 
# whether any assigned entry
# in the specified row matches 
# the given number.
def used_in_row(arr, row, num):
	for i in range(9):
		if(arr[row][i] == num):
			return True
	return False

# Returns a boolean which indicates 
# whether any assigned entry
# in the specified column matches 
# the given number.
def used_in_col(arr, col, num):
	for i in range(9):
		if(arr[i][col] == num):
			return True
	return False

# Returns a boolean which indicates 
# whether any assigned entry
# within the specified 3x3 box 
# matches the given number
def used_in_box(arr, row, col, num):
	for i in range(3):
		for j in range(3):
			if(arr[i + row][j + col] == num):
				return True
	return False

# Checks whether it will be legal 
# to assign num to the given row, col
# Returns a boolean which indicates 
# whether it will be legal to assign
# num to the given row, col location.
def check_location_is_safe(arr, row, col, num):
	
	# Check if 'num' is not already 
	# placed in current row,
	# current column and current 3x3 box
	return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)

# Takes a partially filled-in grid 
# and attempts to assign values to
# all unassigned locations in such a 
# way to meet the requirements
# for Sudoku solution (non-duplication 
# across rows, columns, and boxes)
def solve_sudoku(arr, start_time = None, time_limit = None):
    if start_time and time_limit and time.time() - start_time > time_limit:
        return False
	# 'l' is a list variable that keeps the 
	# record of row and col in 
	# find_empty_location Function 
    l =[0, 0]
	
	# If there is no unassigned 
	# location, we are done 
    if(not find_empty_location(arr, l)):
        return True
	
	# Assigning list values to row and col 
	# that we got from the above Function 
    row = l[0]
    col = l[1]
	
	# consider digits 1 to 9
    for num in range(1, 10):

    # if looks promising
        if(check_location_is_safe(arr, 
            row, col, num)):

    # make tentative assignment
            arr[row][col]= num

    # return, if success, 
    # ya ! 
            if(solve_sudoku(arr, start_time, time_limit)):
                return True

    # failure, unmake & try again
            arr[row][col] = 0
			
	# this triggers backtracking	 
    return False
def sol(quiz, time_limit = None):
    quiz = np.array([[int(quiz[i * 9 + j]) for j in range(9)] for i in range(9)]).tolist()
    global start
    start = time.time()
    if solve_sudoku(quiz, start, time_limit):
        return ''.join(''.join(str(quiz[i][j]) for j in range(9)) for i in range(9))
    return False

# The above code has been contributed by Harshit Sidhwa.
