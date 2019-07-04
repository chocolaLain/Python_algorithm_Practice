class BinTreeNodeError(ValueError):
    pass

# 二叉树结点类
class BinTNode(object):
    """二叉树节点类"""
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right
# end of class


# 统计树中结点个数
def count_BinTNodes(t):
    if t is None:
        return 0  
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


# 假设结点中保存数值，求这种二叉树里的所有数值和。
def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNode(t.left) + sum_BinTNode(t.right)

# 先根序遍历二叉树
def preorder(t, proc):
    if t is None:
        return
    assert(isinstance(t, BinTNode)) # assert(isinstance())是啥?
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


# 中根序遍历二叉树
def inorder(t, proc):
    if t is None:
        return
    inorder(t.left, proc)
    proc(t.data)
    inorder(t.right, proc)
        

# 后根序遍历二叉树
def postorder(t, proc):
    if t is None:
        return
    postorder(t.left, proc)
    postorder(t.right, proc)
    proc(t.data)


# 基于Python list 实现的队列类（循环顺序对列）
class QueueUnderflow(ValueError):
    pass


class SQueue():
    """docstring for SQueue"""
    def __init__(self, init_len = 8):
        self._len = init_len # length of mem-block
        self._elems = [0]*init_len
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
        self._num += 1


    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1


    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0



# 宽度优先遍历二叉树
def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        t = q.dequeue()
        if t is None:
            continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.data)


# 基于python list 实现的栈类
class StackUnderflow(ValueError):
    pass


class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems


    def top(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems[-1]


    def push(self, elem):
        self._elems.append(elem)


    def pop(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems.pop()


# 非递归的先根序遍历二叉树
def preorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t: # go down along left chain
            s.push(t.right) # push right branch into stack
            proc(t.data)
            t = t.left
        t = s.pop() # left chain ends, backtrack


# 非递归的中根序遍历二叉树
def inorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


# 非递归的后根序遍历二叉树
def postorder_nonrec(t, proc):
    s = SStack()
    while t or not s.is_empty():
        while t: # iterate until top has no child
            s.push(t)
            t = t.left if t.left else t.right
            # if we can go left, go, otherwise, go right
        t = s.pop() # get the node to be access
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right # end of left visit, turn right
        else:
            t = None # end of right visit, force to backtrack


# 通过生成器函数遍历
def preorder_elements(t):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


# 打印输出二叉树
def print_BinTNodes(t):
    if t is None:
        print("^", end = "")
        return
    print("(" + str(t.data), end = "")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")", end = "")


# 定义二叉树类和相关操作
class BinTree:
    def __init__(self):
        self._root = None


    def is_empty(self):
        return self._root is None


    def set_root(self, rootnode):
        self._root = rootnode


    def set_left(self, leftchild):
        self._root.left = leftchild


    def set_right(self, rightchild):
        self._root.right = rightchild


    def root(self):
        return self._root


    def leftchild(self):
        return self._root.left


    def rightchild(self):
        return self._root.right


    def preorder_elements(self):
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t.right)
                yield t.data
                t = t.left
                t = s.pop()



if __name__ == '__main__':
    t1 = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))


    print_BinTNodes(t1)
    print()


    preorder(t1, lambda x : print(x, end = ""))
    print()


    preorder_nonrec(t1, lambda x : print(x, end = ""))
    print()


    inorder(t1, lambda x : print(x, end = ""))
    print()


    inorder_nonrec(t1, lambda x : print(x, end = ""))
    print()


    postorder(t1, lambda x : print(x, end = ""))
    print()


    postorder_nonrec(t1, lambda x : print(x, end = ""))
    print()


    for x in preorder_elements(t1):
        print(x)







        

                            