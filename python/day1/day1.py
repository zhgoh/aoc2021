#!/usr/bin/env python3
from load_file import simple_load_int

def first(lst: list) -> None:
    count = 0
    prev = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > prev:
            count += 1
        prev = lst[i]
    print(count)


def second(lst: list) -> None:
    count = 0
    prev = (lst[0], lst[1], lst[2])
    for i in range(1, len(lst) - 2):
        curr = (lst[i], lst[i+1], lst[i+2])
        if sum(curr) > sum(prev):
            count += 1
        prev = curr
    print(count)

def day_1():
    #ls = simple_load_int("day1/sample.txt")
    ls = simple_load_int("day1/input.txt")
    first(ls)
    second(ls)
