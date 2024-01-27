#!/usr/bin/env python3
from load_file import simple_load_csv

def first(ls: list) -> None:
    ls = ls.copy()
    # Set an end marker, anything behind marker considered first cycle
    for day in range(80):
        #print(f"After {day} day(s): {ls}")

        add = 0
        for i in range(len(ls)):
            if ls[i] == 0:
                add += 1
                ls[i] = 7
            ls[i] -= 1
        ls.extend([8 for _ in range(add)])
    print(len(ls))

# Ref: https://www.liamdbailey.com/post/advent-of-code-day-6/
def second(ls: list) -> None:
    ls = ls.copy()
    groups = [0 for _ in range(9)]

    for age in ls:
        groups[age] += 1

    for day in range(256):
        grow = groups[0]

        for i in range(8):
            groups[i] = groups[i + 1]

        # Add new fish to age 8
        groups[8] = grow

        # Add those that have reached age 0
        groups[6] += grow

    print(sum(groups))


def day_6():
    #ls = simple_load_csv("day6/sample.txt", int)
    ls = simple_load_csv("day6/input.txt", int)
    first(ls)
    second(ls)
