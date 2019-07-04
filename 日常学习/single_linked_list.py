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


    def is_empty(self):
        """链表是否为空"""
        return self.__head == None


    def length(self):
        """链表长度"""
        # cur游标用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end = ",")
            cur = cur.next
        print("\n")


    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node


    def append(self, item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty(): # 判断链表为空的情况
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None: # 要将游标停在最后一个节点那里，而不是停在None那里。
                cur = cur.next
            # 最后cur的位置停在了最后一个节点那里
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
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
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是不是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next

                else:
                    pre.next = cur.next
                break # 删完后退出循环
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
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