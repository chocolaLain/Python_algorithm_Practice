class Node(object):
    """二叉树节点"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None
    

class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None # 根节点


    def add(self, item):
        node = Node(item) # Produce a node
        if self.root == None:
            '''队列为空的特殊情况'''
            self.root = node
            return
        queue = [self.root] # add a root into queue

        while queue:
            cur_node = queue.pop(0) # 将根节点从队列中取出，查看这个根节点有无左右孩子
            '''一直执行，直到取到空'''
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
                '''如果左孩子为空，就添加一个左孩子。'''
            else:
                queue.append(cur_node.lchild)
                '''如果左孩子存在，就将他添加到队列中，供之后检查'''

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
                '''同上，左右子节点供之后检查'''
        


    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end = " ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)


    def preorder(self, node): # 传入一个根节点，使得该函数可以递归
        '''先序遍历'''
        if node is None:
            return
        print(node.elem, end = " ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)


    def midorder(self, node): # 传入一个根节点，使得该函数可以递归
        '''中序遍历'''
        if node is None:
            return
        self.midorder(node.lchild)
        print(node.elem, end = " ")
        self.midorder(node.rchild)


    def rearorder(self, node): # 传入一个根节点，使得该函数可以递归
        '''后序遍历'''
        if node is None:
            return
        self.rearorder(node.lchild)
        self.rearorder(node.rchild)
        print(node.elem, end = " ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("")
    tree.preorder(tree.root) # 需要输入根节点
    print("")
    tree.midorder(tree.root) # 需要输入根节点
    print("")
    tree.rearorder(tree.root) # 需要输入根节点