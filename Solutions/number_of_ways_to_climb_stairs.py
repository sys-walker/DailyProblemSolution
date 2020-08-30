#!/bin/python3
class queue:
    def __init__(self):
        self.__theStack = []

    def enqueue(self, val):
        self.__theStack.append(val)

    def dequeue(self):
        self.__theStack.pop(0)

    def rear(self):
        return self.__theStack[0]

    def front(self):
        return self.__theStack[len(self.__theStack) - 1]


def staircase(n):
    # Fill this in.
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n - 2) + staircase(n - 1)


def iterative_staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        q = queue()
        q.enqueue(1)
        q.enqueue(2)
        acc, i = 0, 3
        while i < n + 1:
            acc = q.front() + q.rear()
            q.enqueue(acc)
            q.dequeue()

            i += 1
        return acc


if __name__ == '__main__':
    print(staircase(4))
    # 5
    print(staircase(5))
    # 8
    print(iterative_staircase(4))
    # 5
    print(iterative_staircase(5))
    # 8
