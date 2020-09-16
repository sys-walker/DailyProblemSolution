#!/bin/python3

def findKthLargest(list, pos):
    list.sort()
    return list[pos] if pos < len(list) else None


if __name__ == '__main__':
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
    # 5
