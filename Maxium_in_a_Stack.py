#!/usr/bin/python3
class MaxStack:
    def __init__(self):
        # Fill this in.
        self.theStack = []
        self.max = None

    def push(self, x):
        # Fill this in.
        self.theStack.append(x)

    def pop(self):
        # Fill this in.
        self.theStack.pop()

    def Max(self):
        # Fill this in.
        return None if self.theStack==[] else max(self.theStack)

    def __str__(self):
        return str(self.theStack)


if __name__ == '__main__':
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)

    print(s.Max())
    # 3
    s.pop()
    s.pop()

    print(s.Max())
    # 2
