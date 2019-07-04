import time
import sys
# 班级：数字媒体技术夏季班 学号：17321140027 姓名：刘耀祖 题目：第七题
def insertionSort(arr): 
    start_time = time.clock()
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    end_time = time.clock()
    time2 = end_time - start_time
    return arr, time2

def select(arr):
    start_time = time.clock()
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                    
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    end_time = time.clock()
    time2 = end_time - start_time
    return arr,time2

if __name__ == '__main__':

    array = [45, 32, 63, 87, 66, 23, 37, 49]
    select_af, select_time = select(array)
    print(select_af)
    print("选择排序运行时间：%s" % select_time + "s")

    insertion_af, insertion_time = insertionSort(array)
    print(insertion_af)
    print("插入排序运行时间：%s" % insertion_time + "s")

    time_d = select_time - insertion_time # 计算时间差
    if time_d <= 0:
        print("选择排序更快，时间差：%s" % -time_d + "s")
    else:
        print("插入排序更快，时间差：%s" % time_d + "s")