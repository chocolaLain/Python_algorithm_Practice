# @Time    : 4/22 0022 15:58
# @Author  : Lain
class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self._elems = []


    def is_empty(self):
        return self._elems == []


    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]


    def push(self, elem):
        self._elems.append(elem)


    def pop(self):
        if not self._elems:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()



if __name__ == "__main__":
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    st1.push(43)
    st1.push(522)
    st1.pop()
    while not st1.is_empty():
       print(st1.pop())
