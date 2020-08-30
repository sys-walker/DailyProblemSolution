#!/bin/python3

def staircase(n):
    # Fill this in.
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n - 2) + staircase(n - 1)


if __name__ == '__main__':
    print(staircase(4))
    # 5
    print(staircase(5))
    # 8
