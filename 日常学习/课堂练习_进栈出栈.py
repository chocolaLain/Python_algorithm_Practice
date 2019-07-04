# @Time    : 4/22 0022 16:17
# @Author  : Lain

class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_


class StackUnderflow(ValueError):
    pass


class LStack():
    def __init__(self):
        self._top = None


    def is_empty(self):
        return self._top is None


    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem


    def push(self, elem):
        self._top = LNode(elem, self._top)


    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


if __name__ == "__main__":
    from random import randint
    st1 = LStack()


    for i in range(10):
        st1.push(randint(1,10))


    print(st1.pop())
    st1.pop()
    st1.push(20)
    st1.push(100)
    while not st1.is_empty():
        print(st1.pop())