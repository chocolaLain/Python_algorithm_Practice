# @Time    : 5/5 0005 14:46
# @Author  : Lain

# @Time    : 4/18 0018 21:30
# @Author  : Lain
# coding:utf-8


class Node(object):
    # 节点
    def __init__(self, elem):
        self.elem = elem
        self.next = None #一开始并不知道要链接的Next地址在哪里


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        self.__head = node
        if node: # 确定只有一个节点时是真的有一个节点而不是为空。
            # 让节点指向自己
            node.next = node



    def is_empty(self):
        """链表是否为空"""
        return self.__head == None


    def length(self):
        """链表长度"""
        if self.is_empty(): # 特殊情况
            return 0
        # cur游标用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head: # 确保在循环背景下能不循环计算长度，且不用cur是因为防止最开始对比第一个节点时就出错。
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return 
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end = ",")
            cur = cur.next
        # 退出循环，cur指向尾节点，但是尾节点并没有被打印
        print(cur.elem)
        print("\n")


    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        # 退出循环，cur指向尾节点
        node.next = self.__head
        self.__head = node
        cur.next = self.__head


    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty(): # 判断链表为空的情况
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head: # 要将游标停在最后一个节点那里，而不是停在None那里。
                cur = cur.next
            # 最后cur的位置停在了最后一个节点那里
            node.next = self.__head
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item) # add和append可以直接调用，也方便统一功能
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node
    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        if self.is_empty():
            return
        while cur.next != self.__head:
            # 注意上面这个条件和单链表的区别
            if cur.elem == item:
                # 先判断此节点是不是头节点
                # 头节点
                if cur == self.__head:
                    # 先来寻找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 此时rear指向尾节点，而cur指向头节点，需要移除头节点
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return  # 删完后退出循环，不能是break
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点，但没有处理尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 由cur.next == self.__head和cur == self.__head综合得出：可能会有只有一个节点的情况。
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == "__main__":
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(100)
    print(sll.is_empty())
    print(sll.length())

    sll.append(2)
    sll.append(45)
    sll.append(65)
    sll.append(23)
    sll.append(1010)
    sll.add("jojo")
    sll.travel()
    sll.insert(-1, 100)
    sll.travel()
    sll.insert(3, "kaz")
    sll.travel()
    sll.insert(14, "lain")
    sll.travel()
    sll.insert(2, "dio")
    sll.travel()
    sll.remove(100)
    sll.travel()
    sll.remove("dio")
    sll.travel()
    sll.remove(1010)
    sll.travel()

