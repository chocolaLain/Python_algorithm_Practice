class Dequeue(object):
    """双端队列"""


    def __init__(self):
        self.__list = []


    def add_front(self, item):
        """往队列头部添加元素"""
        self.__list.insert(0, item)


    def add_rear(self, item):
        """往队列尾部添加元素"""
        self.__list.append(item)
        


    def pop_rear(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()


    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        


    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []
        


    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    deque = Dequeue()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.pop_front())
    print(deque.pop_front())
    print(deque.pop_rear())
    print(deque.pop_rear())