#!/bin/python3
import math


def num_ways(n, m):
    if n <= 0 or m <= 0:
        return 0
    n = n - 1
    m = m - 1
    return math.factorial((n + m)) / math.factorial(n) * math.factorial(m)


if __name__ == '__main__':
    print(num_ways(2, 3))
    # 2
