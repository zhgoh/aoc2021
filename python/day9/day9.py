#!/usr/bin/env python3
from load_file import simple_load_str

def first(ls: list) -> None:
    LAST_ROW = len(ls)
    LAST_COL = len(ls[0])

    risk = 0
    for row in range(LAST_ROW):
        for col in range(LAST_COL):
            id = int(ls[row][col])
            left, right, top, bottom = True, True, True, True
            if col > 0:
                left = int(ls[row][col-1]) > id
            if (col + 1) < LAST_COL:
                right = int(ls[row][col+1]) > id
            if (row > 0):
                top = int(ls[row-1][col]) > id
            if (row + 1) < LAST_ROW:
                bottom = int(ls[row+1][col]) > id

            if left and right and top and bottom:
                risk += id + 1
    print(risk)


def neighbors(ls: list, row: int, col: int):
    res = []
    LAST_ROW = len(ls)
    LAST_COL = len(ls[0])
    id = int(ls[row][col])

    if col > 0:
        curr = int(ls[row][col-1])
        if curr != 9 and curr > id:
            res.append((row, col-1))

    if (col + 1) < LAST_COL:
        curr = int(ls[row][col+1])
        if curr != 9 and curr > id:
            res.append((row, col+1))

    if (row > 0):
        curr = int(ls[row-1][col])
        if curr != 9 and curr > id:
            res.append((row-1, col))

    if (row + 1) < LAST_ROW:
        curr = int(ls[row+1][col])
        if curr != 9 and curr > id:
            res.append((row+1, col))
    return res



def bfs(ls: list, row: int, col: int) -> int:
    frontier = [(row, col)]
    explored = {(row, col)}

    while len(frontier) > 0:
        current = frontier[0]
        frontier.pop(0)

        for next in neighbors(ls, current[0], current[1]):
            if next not in explored:
                frontier.append(next)
                explored.add(next)
    return len(explored)



def second(ls: list) -> None:
    points = []
    LAST_ROW = len(ls)
    LAST_COL = len(ls[0])

    for row in range(LAST_ROW):
        for col in range(LAST_COL):
            id = int(ls[row][col])
            left, right, top, bottom = True, True, True, True
            if col > 0:
                left = int(ls[row][col-1]) > id
            if (col + 1) < LAST_COL:
                right = int(ls[row][col+1]) > id
            if (row > 0):
                top = int(ls[row-1][col]) > id
            if (row + 1) < LAST_ROW:
                bottom = int(ls[row+1][col]) > id

            if left and right and top and bottom:
                points.append((row, col))

    basins = []
    for point in points:
        basins.append(bfs(ls, point[0], point[1]))
    basins.sort(reverse=True)
    prod = 1
    for i in range(3):
        prod *= basins[i]
    print(prod)


def day_9():
    #ls = simple_load_str("day9/sample.txt")
    ls = simple_load_str("day9/input.txt")
    first(ls)
    second(ls)
