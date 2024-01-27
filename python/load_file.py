#!/usr/bin/env python3

def simple_load(file: str, fn) -> list[str]:
    """
    Load file from text, can transform inputs based on fn
    """
    with open(file, "rt") as in_file:
        lines = [fn(line.strip()) for line in in_file]
        return lines


def simple_load_csv(file: str, fn) -> list[str]:
    """
    Load file from text with comma sep values
    """
    with open(file, "rt") as in_file:
        line = in_file.readline().strip()
        return [fn(num) for num in line.split(',')]


def simple_load_str(file: str) -> list[str]:
    """
    Load file from text and returns a list of string
    """
    return simple_load(file, lambda x : x)


def simple_load_int(file: str) -> list[int]:
    """
    Load file from text and returns a list of int
    """
    return simple_load(file, int)


def simple_load_bingo(file: str) -> list[list]:
    """
    Loads file and return bingo info
    """
    bingo = []
    with open(file, "rt") as in_file:
        # Read first line
        line = in_file.readline().strip().split(",")
        line = [int(id) for id in line]
        bingo.append(line)

        board = []
        for line in in_file:
            line = line.strip()
            if len(line) == 0:
                continue

            line = [int(id) for id in line.split()]
            board.extend(line)

            if len(board) == 25:
                bingo.append(board)
                board = []
    return bingo


def simple_load_vents(file: str) -> list[tuple]:
    results = []
    with open(file, "rt") as in_file:
        for line in in_file:
            line = line.strip().split(" -> ")
            start = line[0].split(",")
            end = line[1].split(",")
            results.append(
                (
                    int(start[0]),
                    int(start[1]),
                    int(end[0]),
                    int(end[1])
                )
            )
    return results


def simple_load_segments(file: str) -> list[tuple]:
    """
    For loading of | seperated values for the digital clock
    thing
    """
    results = []
    with open(file, "rt") as in_file:
        for line in in_file:
            line = line.strip().split("|")
            inputs = line[0].split()
            outputs = line[1].split()
            results.append(
                (
                    tuple(inputs),
                    tuple(outputs)
                )
            )
    return results
