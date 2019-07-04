import time

# 班级：数字媒体技术夏季班 学号：17321140018 姓名：姚博文 题目：第八题

def bubble(arr):
    ''' 冒泡排序 '''
    start_time = time.clock()
    len_sort = len(arr) 
    for i in range(len_sort):
        for j in range(len_sort-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.clock()
    time2 = end_time - start_time
    return arr, time2

def quickSort(arr,low,high): 
    '''快速排序'''
    start_time = time.clock()
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    end_time = time.clock()
    time2 = end_time - start_time
    return arr, time2

def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

if __name__ == '__main__':
    array = [80, 52, 65, 38, 52, 47, 23, 35]
    bubble_af, bubble_time = bubble(array)
    print(bubble_af)
    print("冒泡排序运行时间：%s" % bubble_time + "s")

    n = len(array)
    quick_af, quick_time = quickSort(array, 0, n - 1)
    print(quick_af)
    print("快速排序运行时间：%s" % quick_time + "s")

    time_d = bubble_time - quick_time # 计算时间差
    if time_d <= 0:
        print("冒泡排序更快，时间差：%s" % -time_d + "s")
    else:
        print("快速排序更快，时间差：%s" % time_d + "s")