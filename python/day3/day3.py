#!/usr/bin/env python3
from load_file import simple_load_str


def first(ls: list) -> None:
    MAX = len(ls[0])
    gamma = ""
    epsilon = ""

    for i in range(MAX):
        ones = 0
        zero = 0
        for line in ls:
            bit = line[i]
            if bit == '0':
                zero += 1
            elif bit == '1':
                ones += 1
        if ones > zero:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)


def second(ls: list) -> None:
    MAX = len(ls[0])
    # Oxygen
    o_ls = ls.copy()
    c_ls = ls.copy()

    for i in range(MAX):
        if len(o_ls) > 1:
            # Oxygen
            ones = 0
            zero = 0

            for line in o_ls:
                bit = line[i]
                if bit == '0':
                    zero += 1
                elif bit == '1':
                    ones += 1

            if ones >= zero:
                o_ls = [line for line in o_ls if line[i] == '1']
            else:
                o_ls = [line for line in o_ls if line[i] == '0']

        if len(c_ls) > 1:
            # CO2
            ones = 0
            zero = 0

            for line in c_ls:
                bit = line[i]
                if bit == '0':
                    zero += 1
                elif bit == '1':
                    ones += 1

            if ones >= zero:
                c_ls = [line for line in c_ls if line[i] == '0']
            else:
                c_ls = [line for line in c_ls if line[i] == '1']


    print(int(o_ls[0], 2) * int(c_ls[0], 2))


def day_3():
    #ls = simple_load_str("day3/sample.txt")
    ls = simple_load_str("day3/input.txt")
    first(ls)
    second(ls)
