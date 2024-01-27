#!/usr/bin/env python3
from load_file import simple_load_str


def transform(ls: list) -> list:
    res = []
    for line in ls:
        items = line.split(" ")
        direction = items[0]
        unit = int(items[1])
        res.append((direction, unit))
    return res


def first(ls: list[str]) -> None:
    ls = transform(ls)
    hor = 0
    dep = 0
    for line in ls:
        direction = line[0]
        unit = line[1]

        if direction == "forward":
            hor += unit
        elif direction == "up":
            dep -= unit
        elif direction == "down":
            dep += unit
    print(dep * hor)


def second(ls: list):
    ls = transform(ls)
    hor = 0
    dep = 0
    aim = 0
    for line in ls:
        direction = line[0]
        unit = line[1]

        if direction == "forward":
            hor += unit
            dep += aim * unit
        elif direction == "up":
            aim -= unit
        elif direction == "down":
            aim += unit
    print(hor * dep)


def day_2():
    #ls = simple_load_str("day2/sample.txt")
    ls = simple_load_str("day2/input.txt")
    first(ls)
    second(ls)
