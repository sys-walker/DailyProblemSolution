#!/bin/python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        c = self.listToNum(l1) + self.listToNum(l2)
        c = list(map(int, str(c)))

        l = self.makeList(c)
        return l

    def listToNum(self, l1):
        iterator = l1
        i, c = 0, 0
        while iterator != None:
            c = c + (pow(10, i) * iterator.val)
            i += 1
            iterator = iterator.next
        return c

    def makeList(self, c):

        result = None
        for e in c:
            result = self.add(result, e)
        return result

    def add(self, node, e):

        if node == None:
            node = ListNode(e)
        else:
            aux = node
            node = ListNode(e)
            node.next = aux
        return node


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
    # 7 0 8
