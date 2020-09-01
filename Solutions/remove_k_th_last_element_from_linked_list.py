#!/bin/python3

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head, k):
    node = head
    i = 0
    while i < k - 2:
        node = node.next
        i += 1
    aux = node.next.next
    node.next = aux
    return head


if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(head)
    # [1, 2, 3, 4, 5]
    head = remove_kth_from_linked_list(head, 3)
    print(head)
    # [1, 2, 4, 5]
