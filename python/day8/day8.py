#!/usr/bin/env python3
from load_file import simple_load_segments

def first(ls: list) -> None:
    count = 0
    for line in ls:
        for signal in line[1]:
            # Count number of strokes
            if len(signal) == 2:
                # 1
                count += 1
            elif len(signal) == 3:
                # 7
                count += 1
            elif len(signal) == 4:
                # 4
                count += 1
            elif len(signal) == 7:
                # 8
                count += 1
    print(count)


def second(ls: list) -> None:
    # 1. Go through each signals
    # 2. Find 1, 4, 7, 8
    # 3. Map remaining configurations
    # 4. Find the number corresponding to the configurations

    total = 0
    for line in ls:
        signals = sorted(line[0], key=len)
        # 9 and 4
        # 3, 4, 5

        ONE = signals[0]
        FOUR = signals[2]
        SEVEN = signals[1]
        EIGHT = signals[9]

        # Find 9 (9 and 4)
        for item in (signals[6], signals[7], signals[8]):
            found = True
            for alpha in FOUR:
                if alpha not in item:
                    found = False
                    break
            if found:
                NINE = item
                break

        # Find 6 (6 and 1, share only 1 segment)
        for item in (signals[6], signals[7], signals[8]):
            count = 0
            for alpha in item:
                if alpha in ONE:
                    count += 1
            if count == 1:
                SIX = item
                break

        # Left zero
        for item in (signals[6], signals[7], signals[8]):
            if item != NINE and item != SIX:
                ZERO = item

        # 5 with 6
        for item in (signals[3], signals[4], signals[5]):
            found = True
            for alpha in item:
                if alpha not in SIX:
                    found = False
            if found:
                FIVE = item
                break

        # Find 3 (3 and 9)
        for item in (signals[3], signals[4], signals[5]):
            if item == FIVE:
                continue
            found = True
            for alpha in item:
                if alpha not in NINE:
                    found = False
                    break
            if found:
                THREE = item
                break

        # Left 2
        for item in (signals[3], signals[4], signals[5]):
            if item != THREE and item != FIVE:
                TWO = item

        nums = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)
        nums = tuple([''.join(sorted(num)) for num in nums])

        res = 0
        for output in line[1]:
            res *= 10
            output = ''.join(sorted(output))
            for i in range(len(nums)):
                if output == nums[i]:
                    res += i
        total += res
    print(total)


def day_8():
    #ls = simple_load_segments("day8/sample.txt")
    ls = simple_load_segments("day8/input.txt")
    first(ls)
    second(ls)
