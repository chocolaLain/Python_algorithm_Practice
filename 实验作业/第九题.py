import time
# 班级：数字媒体技术夏季班 学号：17321140039 姓名：周诗琪 题目：第九题
def merge(a, b):
    '''归并'''
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    

    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    
    return merge(left, right)


def radix_sort(s):
    """基数排序"""
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        print(bucket_list)
        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
        i += 1

    return s

if __name__ == '__main__':
    
    a = [132, 313, 220, 11, 202, 301, 32, 103]
    start_time = time.clock()
    msort = merge_sort(a)
    end_time = time.clock()
    duration01 = end_time - start_time
    print(msort)
    print('归并排序持续时间：%s' % duration01 + 's')

    start_time = time.clock()
    rsort = radix_sort(a)
    end_time = time.clock()
    duration02 = end_time - start_time
    print(rsort)
    print('基数排序持续时间：%s' % duration02 + 's')

    time_difference = duration01 - duration02
    if time_difference <= 0:
        print("归并排序更快，时间差：%s" % -time_difference + "s")
    else:
        print("基数排序更快，时间差：%s" % time_difference + "s")

