#!/usr/bin/env python3
from load_file import simple_load_csv

def first(ls: list) -> None:
    ls = ls.copy()
    ls.sort()

    mid = len(ls) >> 1
    median = ls[mid]

    cost = 0
    for point in ls:
       cost += abs(point - median)
    print(cost)


def second(ls: list) -> None:
    ls = ls.copy()
    ls.sort()

    cost = lambda n: int((n / 2) * (1 + n))

    max_elem = max(ls)
    costs = {}
    for i in range(max_elem):
        if i not in costs:
            costs[i] = 0

        for num in ls:
            costs[i] += cost(abs(num - i))


    print(min(costs.values()))



def day_7():
    #ls = simple_load_csv("day7/sample.txt", int)
    ls = simple_load_csv("day7/input.txt", int)
    first(ls)
    second(ls)
