#!/usr/bin/env python3
from load_file import simple_load_vents

def print_board(board: list, width: int) -> None:
    for i in range(0, len(board), width):
        for s in range(width):
            id = board[i + s]
            if id == 0:
                id = '.'
            print(id, end='')
        print()


def board_size(ls: list) -> tuple:
    # Get max size of board
    maxX = 0
    maxY = 0
    for coord in ls:
        maxX = max(maxX, max(coord[0], coord[2]))
        maxY = max(maxY, max(coord[1], coord[3]))
    return maxX + 1, maxY + 1


def board_count(board: list) -> int:
    count = 0
    for b in board:
        if b > 1:
            count += 1
    return count


def first(ls: list) -> None:
    # Filter vertical/horizontal lines
    new_ls = []
    for coord in ls:
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]

        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            new_ls.append((x1, y1, x2, y2))
    ls = new_ls
    maxX, maxY = board_size(ls)

    # Make board and plot coordinates
    board = [0 for i in range(maxX * maxY)]
    for coord in ls:
        if coord[0] == coord[2]:
            for y in range(coord[1], coord[3] + 1):
                board[y * maxY + coord[0]] += 1
        else:
            for x in range(coord[0], coord[2] + 1):
                board[coord[1] * maxY + x] += 1

    #print_board(board, maxX)
    print(board_count(board))


def second(ls: list) -> None:
    maxX, maxY = board_size(ls)

    # Make board and plot coordinates
    board = [0 for i in range(maxX * maxY)]

    for coord in ls:
        startX = coord[0]
        startY = coord[1]
        endX = coord[2]
        endY = coord[3]

        dirX = 0 if startX == endX else 1 if startX < endX else -1
        dirY = 0 if startY == endY else 1 if startY < endY else -1

        while True:
            board[startY * maxY + startX] += 1

            if dirX == 0 and dirY == 0:
                break

            startX += dirX
            startY += dirY

            if startX == endX:
                dirX = 0
            if startY == endY:
                dirY = 0
    #print_board(board, maxX)
    print(board_count(board))


def day_5():
    #ls = simple_load_vents("day5/sample.txt")
    ls = simple_load_vents("day5/input.txt")
    first(ls)
    second(ls)
