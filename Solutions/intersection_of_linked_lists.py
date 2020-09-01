#!/bin/python3
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


def getCount(head):
    node = head
    count = 0
    while node:
        count += 1
        node = node.next
    return count


def intersection(a, b):
    # fill this in.
    c1 = getCount(a)
    c2 = getCount(b)
    n = abs(c1 - c2)
    i = 0
    largest = None

    if c1 > c2:
        largest = a
    else:
        largest = b

    while i < n:
        largest = largest.next
        i += 1
    return largest.next


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    c.prettyPrint()
    # 3 4
