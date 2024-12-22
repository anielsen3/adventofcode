import sys
import re

input_ = list(map(str.strip, sys.stdin))

# read boards
boards = []
board = []
for line in input_[1:][::-1]: # reverse lines except first line
    if (line):
        board.append(list(map(int, re.split(" +", line))))
    else:
        boards.append(board)
        board = []

# draw numbers
def check_for_win(drawn_numbers, board):
    for row in board:
        if is_subset(row, drawn_numbers):
            return True

    for idx in range(len(board[0])):
        col = list(map(lambda x: x[idx], board))
        if is_subset(col, drawn_numbers):
            return True

    return False

def is_subset(n, m):
    return all(elem in m for elem in n)

def all_numbers(board):
    return [item for sublist in board for item in sublist]

def unmarked_numbers(board, drawn_numbers):
    return [x for x in all_numbers(board) if x not in drawn_numbers]

def print_board(board):
    for row in board[::-1]:
        print(" ".join(map(str, row)))

drawn_numbers = []
for drawn_num in map(int, input_[0].split(",")):
    drawn_numbers += [drawn_num]
    for board in boards:
        if check_for_win(drawn_numbers, board):
            sum_unmarked = sum(unmarked_numbers(board, drawn_numbers))
            last_num = drawn_numbers[-1]
            print(sum_unmarked, last_num, sum_unmarked * last_num) 
            boards.remove(board)
