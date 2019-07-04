# @Time    : 5/6 0006 17:09
# @Author  : Lain


class QueueUnderflow(ValueError):
    pass


class SQueue():
    def __init__(self, init_len = 8):
        self._len = init_len # length of em-block
        self._elems = [0] * init_len
        self._head = 0 # index of head element
        self._num = 0 # number of elements

    def is_empty(self):
        return self._num == 0


    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]


    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e


    def enqueue(self, elem):
        if self._num == self._len:
            self._extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1


    def _extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) %old_len]
        self._elems, self._head = new_elems, 0



from random import randint


if __name__ == '__main__':
    q = SQueue()
    s = 0
    for j in range(20):
        for i in range(randint(1, 200)):
            q.enqueue(i*3)
            s += 1
        for i in range(randint(1, 20)):
            if not q.is_empty():
                print(q.dequeue())

    q.enqueue(100)
    while not q.is_empty():
        print(q.dequeue())
    print("s=", s)
