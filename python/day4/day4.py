#!/usr/bin/env python3
from load_file import simple_load_bingo

def print_board(board: list[int]) -> None:
    for i in range(0, 25, 5):
        print(f"{board[i]} {board[i+1]} {board[i+2]} {board[i+3]} {board[i+4]}")

def check_vertical(board: list[int]) -> bool:
    for c in range(5):
        count = 0
        for r in range(5):
            if board[r * 5 + c] == -1:
                count += 1
        if count == 5:
            return True
    return False


def check_horizontal(board: list[int]) -> bool:
    for r in range(5):
        count = 0
        for c in range(5):
            if board[r * 5 + c] == -1:
                count += 1
        if count == 5:
            return True
    return False


def sum_unmarked(board: list[int]) -> int:
    total = 0
    for num in board:
        if num == -1:
            continue
        total += num
    return total


def first(ls: list) -> None:
    numbers = ls[0]
    boards = []
    for i in range(1, len(ls)):
        # Create a new copy
        boards.append(list(ls[i]))

    # 1. Find the first winning board
    # 2. Find sum of unmarked
    # 3. Multiply sum with winning number
    for number in numbers:
        for board in boards:
            for i in range(25):
                if board[i] == number:
                    board[i] = -1
            if check_horizontal(board) or check_vertical(board):
                print(number * sum_unmarked(board))
                return


def second(ls: list) -> None:
    numbers = ls[0]
    boards = []

    for i in range(1, len(ls)):
        boards.append(list(ls[i]))

    wins = [False for i in range(len(boards))]

    # 1. Find the last winning board
    # 2. Find sum of unmarked
    # 3. Multiply sum with winning number
    curr_num = 0
    unmarked = 0
    for number in numbers:
        for b in range(len(boards)):
            board = boards[b]
            for i in range(25):
                if board[i] == number:
                    board[i] = -1

            if check_horizontal(board) or check_vertical(board):
                wins[b] = True
                unmarked = sum_unmarked(board)
                if wins.count(False) == 0:
                    print(number * unmarked)
                    return


def day_4():
    #ls = simple_load_bingo("day4/sample.txt")
    ls = simple_load_bingo("day4/input.txt")
    first(ls)
    second(ls)
