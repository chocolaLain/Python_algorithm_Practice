# coding:utf-8

class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = [] # 私有属性，防止有人不通过push和pop直接对我们的list进行操作


    def push(self, item):
        """追加一个新的元素到栈顶"""
        self.__list.append(item)
        pass


    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()
        pass 


    def peek(self):
        """返回栈顶元素"""
        if self.__list: # 考虑空链表情况
            return self.__list[-1]
        else:
            return None
        pass


    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # return not self.__list 这种方式也可以

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)
        pass


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())