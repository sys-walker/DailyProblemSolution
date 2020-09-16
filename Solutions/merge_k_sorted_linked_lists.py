#!/bin/python3
import heapq


class Integer_Max_Heap:
    def __init__(self):
        self.array = []
        self.size = 0

    def add(self, other):
        self.array.append(-1 * other)
        heapq.heapify(self.array)
        self.size += 1

    def remove(self):
        if self.size == 0:
            return None
        r = heapq.heappop(self.array)
        self.size -= 1
        return -1 * r

    def __str__(self):
        return str(self.array)


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) + " " if c.val else ""
            c = c.next
        return answer

    @classmethod
    def createNode(cls, val, list):

        if list == None:
            list = Node(val, None)
            return list
        else:
            l = Node(val, list)
            return l


def merge(nums):
    auxiliar = Integer_Max_Heap()
    for list in nums:
        while list:
            auxiliar.add(list.val)
            list = list.next
    result = None
    while auxiliar.size != 0:
        result = Node.createNode(auxiliar.remove(), result)
    return result


if __name__ == '__main__':
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))

    print(merge([a, b]))
