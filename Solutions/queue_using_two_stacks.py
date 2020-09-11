#!/bin/python3

class Queue:
    def __init__(self):
        self.stack_enq = []
        self.stack_deq = []

    def enqueue(self, val):
        self.stack_enq.append(val)

    def dequeue(self):
        if len(self.stack_enq) == 0 and len(self.stack_deq) == 0:
            return None
        elif self.stack_deq == []:
            self.switch_stack()
        return self.stack_deq.pop()

    def switch_stack(self):
        while self.stack_enq:
            self.stack_deq.append(self.stack_enq.pop())


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    # 1 2 3
