# @Time    : 5/6 0006 17:31
# @Author  : Lain


# 定义一个节点
class QueueNode:
    def __init__(self):
        self.data = None
        self.next = None


# 类说明：定义一个链式队列
class LinkQueue:
    # 默认的初始化队列的函数
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode


    #判断对列是否为空的函数
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue


    # 入队的函数
    def EnQueue(self, data):
        tQueueNode = QueueNode()
        tQueueNode.data = data
        self.rear.next = tQueueNode
        self.rear = tQueueNode
        print("当前进队的元素为：", data)


    # 出队的函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            return self.front.next.data


    # 由用户输入元素将其进队的函数
    def CreateQueueByInput(self):
        data = input("请输入元素（继续输入请按回车，结束输入请按‘#’):")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")



# 主程序
lq = LinkQueue()
lq.CreateQueueByInput()
print(lq.IsEmptyQueue())