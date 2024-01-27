#!/usr/bin/env python3
from load_file import simple_load_str

def first(ls: list) -> None:
    #print(ls)
    illegal = []
    for line in ls:
        stack = []
        for char in line:
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    illegal.append(char)
                    break
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    illegal.append(char)
                    break
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    illegal.append(char)
                    break
            elif char == '>':
                if stack[-1] == '<':
                    stack.pop()
                else:
                    illegal.append(char)
                    break
            else:
                stack.append(char)
    res = 0
    table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for char in illegal:
        res += table[char]
    print(res)


def second(ls: list) -> None:
    missing = []
    for line in ls:
        stack = []
        for char in line:
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.clear()
                    break
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.clear()
                    break
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.clear()
                    break
            elif char == '>':
                if stack[-1] == '<':
                    stack.pop()
                else:
                    stack.clear()
                    break
            else:
                stack.append(char)
        if len(stack) > 0:
            missing.append(stack)

    scores = []
    # Note: symbols in stack are reversed, because those are incomplete
    table = {'(': 1, '[': 2, '{': 3, '<': 4}

    for line in missing:
        score = 0
        # Order of checking matters
        for char in reversed(line):
            score *= 5
            score += table[char]
        scores.append(score)

    scores.sort()
    print(scores[len(scores) >> 1])


def day_10():
    #ls = simple_load_str("day10/sample.txt")
    ls = simple_load_str("day10/input.txt")
    first(ls)
    second(ls)
