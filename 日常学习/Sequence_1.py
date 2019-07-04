# @Time    : 5/6 0006 16:46
# @Author  : Lain


class SequenceQueue:
    # 默认的初始化队列的函数

    def __init__(self):
        self.MaxQueueSize = 10
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0


    # 判断对列是否为空的函数
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue


    # 元素入队的函数
    def EnQueue(self, x):
        if(self.rear < self.MaxQueueSize - 1):
            self.rear = self.rear + 1
            self.s[self.rear] = x
            print("当前进队元素为:", x)
        else:
            print("队列已满，无法入队")
            return


    # 元素出队的函数
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法入队")
            return
        else:
            self.front = self.front + 1
            return self.s[self.rear]


    # 获取当前队首元素的函数
    def GetHead(self):
        if self.IsEmptyQueue():
            print("队列为空，无法输出队首元素")
            return
        else:
            return self.s[self.front + 1]


    # 由用户输入元素将其进队的函数
    def CreateQueueByInput(self):
        data = input("请输入元素（继续输入请按回车，结束输入请按“#”)：")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素：")



# 主程序

sq = SequenceQueue()
print(sq.IsEmptyQueue())
sq.CreateQueueByInput()
print(sq.IsEmptyQueue())
print(sq.GetHead())
sq.DeQueue()
sq.DeQueue()
sq.DeQueue()
sq.DeQueue()
sq.DeQueue()
sq.DeQueue()
print(sq.GetHead())