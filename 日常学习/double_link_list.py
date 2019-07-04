class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.Prev = None

class DoubleLinkList(object):
    """单链表"""
    def __init__(self, node = None):
        self.__head = node


    def is_empty(self):
        """链表是否为空"""
        return self.__head is None


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
        if node.next is None:
            return 
        else:
            node.next.prev = node


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
            node.prev = cur


    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = cur 
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
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
                    if cur.next:
                        # 考虑只有一个节点的情况
                        cur.next.prev == None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 考虑尾节点的情况
                        cur.next.prev = cur.prev
                break # 删完后退出循环
            else:
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
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(100)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.append(45)
    dll.append(65)
    dll.append(23)
    dll.append(1010)
    dll.add("jojo")
    dll.travel()
    dll.insert(-1, 100)
    dll.travel()
    dll.insert(3, "kaz")
    dll.travel()
    dll.insert(14, "lain")
    dll.travel()
    dll.insert(2, "dio")
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove("dio")
    dll.travel()
    dll.remove(1010)
    dll.travel()

        